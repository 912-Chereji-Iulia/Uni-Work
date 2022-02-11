import datetime
from datetime import date, datetime

from domain.activity import ActivityValidator, Activity
from domain.person import Person
from iterator import shell_sort, _filter
from repository.activity_repo import ActivityRepo, ActivityRepoExceptions
from repository.person_repo import PersonRepo, PersonRepoException
from repository.undo_service import FunctionCall, Operation, CascadedOperation


class ActivityService:
    def __init__(self,activity_repo:ActivityRepo, validator:ActivityValidator,undo,person_repo:PersonRepo):
        self._activity_repo=activity_repo
        self._validator=validator
        self._undo=undo
        self._person_repo=person_repo


    @property
    def activities(self):
        """
        the list of all activities in the repository
        :return:
        """

        return self._activity_repo.activities

    def add(self, activity:Activity):
        """
        Adds a new activity to the repository if possible
        :param activity:
        :return:
        """
        self.update_activity_repo()
        for i in range(len(activity.person_ids)):
            if self._person_repo.person_in_list(activity.person_ids[i]) == False:
                raise ActivityRepoExceptions("Person with this id is not in the planner.")
        self._validator.valid_activity(activity)
        self._activity_repo.add_activity(activity)
        undo_fun = FunctionCall(self._activity_repo.remove_activity, activity.activity_id)
        redo_fun = FunctionCall(self._activity_repo.add_activity, activity)
        o = Operation(undo_fun, redo_fun)
        self._undo.record(o)

    def remove(self, act_id):
        """
        removes an activity from the repo by a given id
        :param act_id:
        :return:
        """
        self.update_activity_repo()
        activities = _filter(self.activities, lambda act: act.activity_id == act_id)
        ok = False
        if activities != []:
            ok = True
        if not ok:
            raise ActivityRepoExceptions("The activity with the given id is not in the agenda!")
        activity = activities[0]
        self._activity_repo.remove_activity(act_id)
        undo_fun = FunctionCall(self._activity_repo.add_activity, activity)
        redo_fun = FunctionCall(self._activity_repo.remove_activity, activity.activity_id)
        o = Operation(undo_fun, redo_fun)
        self._undo.record(o)

    def update(self, act_id,person_ids,date,start_time,end_time,desc):
        """
        updates an activity
        :param activity:
        :return:
        """

        ok1 = True
        for i in person_ids:
            if self._person_repo.person_in_list(i) == False:
                raise ActivityRepoExceptions("Person with this id is not in the planner.")
        if ok1:
            self.update_activity_repo()
            activities=_filter(self.activities,lambda act: act.activity_id ==act_id)
            ok = False
            if activities != []:
                ok = True
            if not ok:
                raise ActivityRepoExceptions("The activity with the given id is not in the agenda!")
            activity=activities[0]
            previous_date = activity.date
            previous_start_time = activity.start_time
            previous_end_time = activity.end_time
            previous_desc = activity.description
            previous_persons_ids = activity.person_ids
            self._validator.valid_activity(Activity(act_id,person_ids, date, start_time, end_time, desc ))
            self._activity_repo.update_activity(act_id,person_ids, date, start_time, end_time, desc )
            undo_fun = FunctionCall(self._activity_repo.update_activity, act_id,previous_persons_ids, previous_date, previous_start_time,
                                    previous_end_time, previous_desc )
            redo_fun = FunctionCall(self._activity_repo.update_activity, act_id,person_ids, date, start_time, end_time, desc)
            o = Operation(undo_fun, redo_fun)
            self._undo.record(o)

    def update_activity_repo(self):
        extra=[]
        for act in self.activities:
            for el in act.person_ids:
                if not self._person_repo.person_in_list(el):
                    act.person_ids.remove(el)    #remove a person that was removed
                    undo_fun = FunctionCall(act.person_ids.append, el)
                    redo_fun = FunctionCall(act.person_ids.remove, el)
                    o = Operation(undo_fun, redo_fun)
                    extra.append(o)
        if self._undo.return_index() > -1:   #bring it back to all the activities
            if self._undo.normal_operation():
                first_func, second_func = self._undo.separate_last_op()
                if first_func.function_ref() == self._person_repo.add_person and second_func.function_ref() == self._person_repo.remove_person:
                    op = Operation(first_func,second_func)
                    co = CascadedOperation(op, *extra)
                    self._undo.remove_last_element()
                    self._undo.record(co)
        return None

    def get_all(self):
        self.update_activity_repo()
        return self._activity_repo.get_all()

    def search_date_time(self,date,time):
        self.update_activity_repo()
        self._validator.valid_date(date)
        self._validator.valid_time(time)
        list=_filter(self.activities, lambda activity: activity.date.find(date)!=-1 and activity.start_time.find(time)!=-1)
        ok=False
        if list != []:
            ok = True
        if not ok:
            raise ActivityRepoExceptions("The activity with the given date and start time is not in the agenda!")
        return list

    def search_description(self,desc):
        self.update_activity_repo()
        self._validator.valid_description(desc)
        list=_filter(self.activities,lambda activity:activity.description.lower().find(desc.lower())!=-1)
        ok = False
        if list != []:
            ok = True
        if not ok:
            raise ActivityRepoExceptions("The activity with the given description is not in the agenda!")
        return list

    def upcoming_dates(self,gdate,gtime):
        """
        checks if a given date is later than the current date
        :param date:
        :return:
        """
        self.update_activity_repo()
        today = str(date.today())
        today_time = str(datetime.now().strftime("%H:%M:%S"))
        if int(gdate[0:4]) > int(today[0:4]):
            return True
        elif int(gdate[0:4]) == int(today[0:4]) and int(gdate[5:7]) > int(today[5:7]):
            return True
        elif int(gdate[0:4]) == int(today[0:4]) and int(gdate[5:7]) == int(today[5:7]) and \
                int(gdate[8:10]) > int(today[8:]):
            return True
        elif gdate == today:
            if int(gtime[0:2]) > int(today_time[0:2]):
                return True
            elif int(gtime[0:2]) == int(today_time[0:2]) and int(gtime[3:]) > int(today_time[3:5]):
                return True
        return False

    def free_time_in_day(self, gdate):
        day=_filter(self.activities,lambda i:i.date==gdate)
        shell_sort(day, lambda act1,act2: act1.start_time[0:2]<act2.start_time[0:2] or(act1.start_time[0:2] == act2.start_time[0:2] and act1.start_time[3:] < act2.start_time[3:] ))
        t=int(day[0].start_time[0:2])*60+int(day[0].start_time[3:])
        for i in range(len(day)-1):
            t1=int(day[i+1].start_time[0:2])*60+int(day[i+1].start_time[3:])
            t2=int(day[i].end_time[0:2]) * 60 + int(day[i].end_time[3:])
            t=t+t1-t2
        t=t+(23-int(day[len(day)-1].end_time[0:2]))*60+(59-int(day[len(day)-1].end_time[3:]))
        return t


    def st_busiest_days(self):
        """
        the list of the busiest days
        :return:
        """
        busy = _filter(self.activities,lambda act:self.upcoming_dates(act.date,act.start_time))
        busy1 = []
        dates=[]
        for i in busy:
            if i.date not in dates:
                busy1.append(i)
                dates.append(i.date)

        shell_sort(busy1,lambda b1,b2: self.free_time_in_day(b1.date)<self.free_time_in_day(b2.date))
        return busy1


    def st_activities_with_a_person(self, person_id):
        """
        the list of activities with a given person with id equal to person_id
        :param person_id: the given person
        :return:
        """
        result= _filter(self.activities,lambda activity: person_id in activity._person_ids and self.upcoming_dates(activity.date, activity.start_time))
        return result


    def st_activities_for_a_date(self,given_date):
        """
        the list of activities for a given date, displayed in the order of their start time
        :param given_date:
        :return:
        """
        result=_filter(self.activities,lambda act: given_date==act.date)
        shell_sort(result, lambda act1, act2: act1.start_time[0:2] < act2.start_time[0:2] or (act1.start_time[0:2] == act2.start_time[0:2] and act1.start_time[3:] < act2.start_time[3:] ))
        return result


    def __len__(self):
        """
        Returns the length of the repository
        :return:
        """
        return len(self._activity_repo)

