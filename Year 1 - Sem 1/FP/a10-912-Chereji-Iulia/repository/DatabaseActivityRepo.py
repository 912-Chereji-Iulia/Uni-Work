from iterator import IterableObject
from repository.activity_repo import ActivityRepo, Activity
import sqlite3
class DatabaseActivityRepo(ActivityRepo):
    def __init__(self, connection= "activity.db"):
        lst=IterableObject()
        super().__init__(lst)
        self._connection = sqlite3.connect(connection)
        self._cursor = self._connection.cursor()
        self._load()

    def create_table(self):
        self._cursor.execute('''CREATE TABLE ACTIVITY (
        ID TEXT NOT NULL, PERSLIST TEXT NOT NULL, DATE TEXT NOT NULL, STARTTIME TEXT NOT NULL, ENDTIME TEXT NOT NULL, DESCRIPTION TEXT NOT NULL)''')

    def add_activity(self, activity):
        super().add_activity(activity)
        id = activity.activity_id
        date = activity.date
        starttime = activity.start_time
        endtime = activity.end_time
        description = activity.description
        perslist = str(activity.person_ids)
        with self._connection:
            self._cursor.execute("INSERT INTO ACTIVITY (ID, PERSLIST, DATE, STARTTIME, ENDTIME,DESCRIPTION) VALUES (?, ?, ?, ?, ?, ?)",
                             (id, perslist,date, starttime,endtime,description))

    def remove_activity(self,id_act):
        super().remove_activity(id_act)
        with self._connection:
            self._cursor.execute("DELETE from ACTIVITY where ID = :id",{'id':id_act})

    def update_activity(self, id, pers_list, date, starttime, endtime, description):
        super().update_activity(id,pers_list,date,starttime,endtime,description)
        with self._connection:
            self._cursor.execute('''UPDATE ACTIVITY SET PERSLIST = :perslist WHERE ID = :id''',
                                 {"id": id, "perslist": str(pers_list)})

            self._cursor.execute('''UPDATE ACTIVITY SET DATE = :date WHERE ID = :id''',{"id": id,"date": date})
            self._cursor.execute('''UPDATE ACTIVITY SET STARTTIME = :starttime WHERE ID = :id''',{"id": id,"starttime": starttime})
            self._cursor.execute('''UPDATE ACTIVITY SET ENDTIME = :endtime WHERE ID = :id''',{"id": id, "endtime": endtime})
            self._cursor.execute('''UPDATE ACTIVITY SET DESCRIPTION = :description WHERE ID = :id''',{"id": id, "description": description})


    def get_all(self):
        super().get_all()
        self._connection.commit()
        return self._activities


    def _load(self):
        self._cursor = self._connection.execute("SELECT ID, PERSLIST, DATE, STARTTIME, ENDTIME, DESCRIPTION from ACTIVITY")
        for row in self._cursor:
            id =int(row[0])
            date = row[1]
            starttime = row[2]
            endtime = row[3]
            description = row[4]
            pers_list_unpack = row[5].replace('[','').replace(']','').replace('\n','').split(',')
            pers_list =[]
            i = 0
            while i < len(pers_list_unpack)-1:
                person = [pers_list_unpack[i].replace("'",'').strip(),pers_list_unpack[i+1].replace("'",'').strip()]
                pers_list.append(person)
                i = i+2
            self._activities.add(Activity(id, pers_list, date,starttime, endtime,description))