from domain.person import Person
from iterator import IterableObject


class PersonRepoException(Exception):
    def __init__(self, msg):
        self._msg = msg

class PersonRepo:
    def __init__(self,persons:IterableObject):
        self._persons = persons

    @property
    def persons(self):
        return self._persons

    def get_ids(self):
        ids=[]
        for i in self.persons:
            ids.append(i.id)
        return ids

    def person_in_list(self,id):
        """
        checks if a given person is in the agenda
        :param id:
        :return:
        """
        for person in self.persons:
            if id == person.id:
                return True
        return False

    def add_person(self, id,name,phone):
        """
        adds a person to the repository
        :param person:
        :return:
        """
        person=Person(id,name,phone)
        if id in self.get_ids():
            raise PersonRepoException ("Duplicate id!")
        else:
            self._persons.add(person)

    def remove_person(self,id_remove):
        """
        removes a person from the repo

        :param id_remove:
        :return:
        """

        ok=True
        i=0
        while i <= len(self._persons)-1 :
            if  self._persons[i].id==id_remove:
                self._persons.__delitem__(i)
                ok=False
            else:
                i=i+1
        if ok:
            raise PersonRepoException("The person with the given id doesn't exist!")


    def update_person(self,id, name,phone_nr):
        """
        updates a person from the repo
        :param person:
        :return:
        """
        ok=True
        for p in self._persons:
            if id == p.id:
                p._name = name
                p._phone_nr = phone_nr
                ok= False
        if ok:
            raise PersonRepoException("The person to be updated doesn't exist!")

    def get_firstname(self,name):
        tokens=name.split()
        return tokens[0]

    def get_secondname(self,name):
        tokens=name.split()
        if len(tokens)>1:
            return tokens[1]
        else:
            return tokens


    def __len__(self):
        """
        Returns the length of the repository
        :return:
        """
        return len(self._persons)





