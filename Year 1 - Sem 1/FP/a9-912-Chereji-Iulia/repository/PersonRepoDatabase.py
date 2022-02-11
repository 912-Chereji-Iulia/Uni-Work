from repository.person_repo import PersonRepo, Person
import sqlite3
from sqlite3 import Error
class DatabasePeopleRepo(PersonRepo):
    def __init__(self, connection= "person.db"):
        super().__init__([])
        self._connection = sqlite3.connect(connection)
        self._cursor = self._connection.cursor()
        self._load()

    def create_table(self):
        self._cursor.execute('''CREATE TABLE PEOPLE (
        ID TEXT, NAME TEXT, NUMBER TEXT)''')

    def add_person(self, id,name,phone):
        super().add_person(id,name,phone)
        with self._connection:
            self._cursor.execute("INSERT INTO PEOPLE (ID, NAME, NUMBER) VALUES (?, ?, ?)",
                             (id,name, phone))

    def remove_person(self,person_id):
        super().remove_person(person_id)
        with self._connection:
            self._cursor.execute("DELETE from PEOPLE where ID = :id",{'id':person_id})

    def update_person(self,person_id,name,number):
        super().update_person(person_id,name,number)
        with self._connection:
            self._cursor.execute('''UPDATE PEOPLE SET NAME = :name  WHERE ID = :id''',{'name': name,'id': person_id})
            self._cursor.execute('''UPDATE PEOPLE SET NUMBER = :number  WHERE ID = :id''', {'number': number, 'id': person_id})

    def get_all(self):
        super().persons()
        self._connection.commit()
        return self._persons.__copy__()


    def _load(self):
        self._cursor = self._connection.execute("SELECT ID, NAME, NUMBER from PEOPLE")
        for row in self._cursor:
            id =int(row[0])
            name = row[1]
            number = row[2]
            self._persons.append(Person(id,name,number))













