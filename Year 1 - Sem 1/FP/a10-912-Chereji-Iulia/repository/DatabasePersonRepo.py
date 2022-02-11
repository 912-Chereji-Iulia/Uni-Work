from iterator import IterableObject
from repository.person_repo import PersonRepo, Person
import sqlite3
from sqlite3 import Error
class DatabasePeopleRepo(PersonRepo):
    def __init__(self, connection= "person.db"):
        l=IterableObject()
        super().__init__(l)
        self._connection = sqlite3.connect(connection)
        self._cursor = self._connection.cursor()
        self._load()

    def create_table(self):
        self._cursor.execute('''CREATE TABLE PERSONS (
        ID TEXT, NAME TEXT, NUMBER TEXT)''')

    def add_person(self, id,name,number):
        super().add_person(id,name,number)
        with self._connection:
            self._cursor.execute("INSERT INTO PERSONS (ID, NAME, NUMBER) VALUES (?, ?, ?)",
                             (id,name, number))

    def remove_person(self,person_id):
        super().remove_person(person_id)
        with self._connection:
            self._cursor.execute("DELETE from PERSONS where ID = :id",{'id':person_id})

    def update_person(self,id,name,number):
        super().update_person(id,name,number)
        with self._connection:
            self._cursor.execute('''UPDATE PERSONS SET NAME = :name  WHERE ID = :id''',{'name': name,'id': id})
            self._cursor.execute('''UPDATE PERSONS SET NUMBER = :number  WHERE ID = :id''', {'number': number, 'id': id})

    def get_all(self):
        super().persons()
        self._connection.commit()
        return self._persons


    def _load(self):
        self._cursor = self._connection.execute("SELECT ID, NAME, NUMBER from PERSONS")
        for row in self._cursor:
            id = int(row[0])
            name = row[1]
            number = row[2]
            self._persons.add(Person(id,name,number))












