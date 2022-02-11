from repository.activity_repo import ActivityRepo, Activity
import sqlite3
class DatabaseActivityRepo(ActivityRepo):
    def __init__(self, connection= "activity.db"):
        super().__init__([])
        self._connection = sqlite3.connect(connection)
        self._cursor = self._connection.cursor()
        self._load()

    def create_table(self):
        self._cursor.execute('''CREATE TABLE ACTIVITIES (
        ID TEXT NOT NULL, DATE TEXT NOT NULL, STARTTIME TEXT NOT NULL, ENDTIME TEXT NOT NULL, DESCRIPTION TEXT NOT NULL, PERSLIST TEXT NOT NULL )''')

    def add_activity(self, activity):
        super().add_activity(activity)
        id = activity.activity_id
        date = activity.date
        starttime = activity.start_time
        endtime = activity.end_time
        description = activity.description
        perslist = str(activity.person_ids)
        with self._connection:
            self._cursor.execute("INSERT INTO ACTIVITIES (ID, DATE, STARTTIME, ENDTIME,DESCRIPTION, PERSLIST) VALUES (?, ?, ?, ?, ?, ?)",
                             (id,date, starttime,endtime,description,perslist))

    def remove_activity(self,activity):
        super().remove_activity(activity)
        id_act = activity.id
        with self._connection:
            self._cursor.execute("DELETE from ACTIVITIES where ID = :id",{'id':id_act})

    def update_activity(self, activity_id, pers_list, date, start_time, end_time, description):
        super().update_activity(activity_id,pers_list,date,start_time,end_time,description)
        with self._connection:
            self._cursor.execute('''UPDATE ACTIVITIES SET PERSLIST = :perslist WHERE ID = :id''',
                                 {"id": activity_id, "perslist": str(pers_list)})
            self._cursor.execute('''UPDATE ACTIVITIES SET DATE = :date WHERE ID = :id''',{"id": activity_id,"date": date})
            self._cursor.execute('''UPDATE ACTIVITIES SET STARTTIME = :starttime WHERE ID = :id''',{"id": activity_id,"starttime": start_time})
            self._cursor.execute('''UPDATE ACTIVITIES SET ENDTIME = :endtime WHERE ID = :id''',{"id": activity_id, "endtime": end_time})
            self._cursor.execute('''UPDATE ACTIVITIES SET DESCRIPTION = :description WHERE ID = :id''',{"id": activity_id, "description": description})



    def get_all(self):
        super().get_all()
        self._connection.commit()
        return self._activities.__copy__()


    def _load(self):
        self._cursor = self._connection.execute("SELECT ID, DATE, STARTTIME, ENDTIME, DESCRIPTION, PERSLIST from ACTIVITIES")
        for row in self._cursor:
            id = int(row[0])
            date = row[1]
            starttime = row[2]
            endtime = row[3]
            description = row[4]
            pers_list_unpack = row[5].replace('[','').replace(']','').replace('\n','').split(',')
            pers_list =[]
            i = 0
            while i < len(pers_list_unpack)-1:
                person = [pers_list_unpack[i].replace("'",'').strip(),pers_list_unpack[i+1].replace("'",'').strip()]
                person=int(person[0])
                pers_list.append(person)
                i = i+2
            self._activities.append(Activity(id, pers_list, date,starttime, endtime,description))