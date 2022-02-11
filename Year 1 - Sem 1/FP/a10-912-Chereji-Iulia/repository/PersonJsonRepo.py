import json

from iterator import IterableObject
from repository.person_repo import PersonRepo
from domain.person import Person

class PersonJsonRepo(PersonRepo):
    def __init__(self, file_name):
        lst=IterableObject()
        super().__init__(lst)
        self._file_name = file_name
        self._load()

    def _load(self):
        f = open(self._file_name,)
        people_dict = json.load(f)
        for person in people_dict['persons']:
            self._persons.add(Person(person['id'], person['name'], person['phone number']))
        f.close()

    def add_person(self, id, name,phone):
        super().add_person(id,name,phone)
        self._save()

    def remove_person(self,id_remove):
        super().remove_person(id_remove)
        self._save()

    def update_person(self, person_id, name, number):
        super().update_person(person_id,name,number)
        self._save()

    def _save(self):
        with open(self._file_name) as json_file:
            people_dict = json.load(json_file)
            temp = people_dict['persons']
            del temp[:]
            for person in self.persons:
                new_person = {"id": person.id,
                              "name": str(person.name),
                              "phone number": str(person.phone_nr)
                              }
                temp.append(new_person)
        with open(self._file_name,'w') as f:
            json.dump(people_dict,f,indent=4)




