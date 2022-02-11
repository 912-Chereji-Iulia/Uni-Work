import json

from iterator import IterableObject
from repository.activity_repo import ActivityRepo
from domain.activity import Activity
class ActivityJsonRepo(ActivityRepo):
    def __init__(self, file_name):
        lst=IterableObject()
        super().__init__(lst)
        self._file_name = file_name
        self._load()

    def _load(self):
        f = open(self._file_name,)
        activity_dict = json.load(f)
        for activity in activity_dict['activities']:
            self._activities.add(Activity(activity['id'],activity['person list'],activity['date'],activity['start time'],activity['end time'],activity['description']))
        f.close()

    def add_activity(self, act):
        super().add_activity(act)
        self._save()

    def remove_activity(self, id_remove):
        super().remove_activity(id_remove)
        self._save()

    def get_all(self):
        super().get_all()
        self._save()
        return self.activities[:]

    def update_activity(self, activity_id,pers_list, date, start_time, end_time, description ):
        super().update_activity(activity_id,pers_list,date,start_time,end_time,description)
        self._save()

    def _save(self):
        with open(self._file_name) as json_file:
            act_dict = json.load(json_file)
            temp = act_dict['activities']
            del temp[:]
            for activity in self._activities:
                new_activity = {
                    "id": activity.activity_id,
                    "person list": activity.person_ids,
                    "date":str(activity.date),
                    "start time":str(activity.start_time),
                    "end time": str(activity.end_time),
                    "description": str(activity.description)
                }
                temp.append(new_activity)
        with open(self._file_name,'w') as f:
            json.dump(act_dict,f,indent=4)

