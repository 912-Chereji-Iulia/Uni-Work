from domain.person import PersonValidator, Person
from iterator import _filter
from repository.activity_repo import ActivityRepo
from repository.person_repo import PersonRepo, PersonRepoException
from repository.undo_service import FunctionCall, Operation


class PersonService:
    def __init__(self,persons_repo:PersonRepo,validator:PersonValidator,undo):
        self._repo=persons_repo
        self._validator=validator
        self._undo=undo


    @property
    def persons(self):
        return self._repo.persons

    def add(self, id,name,phone):
        """
        adds a person to the agenda
        :param person:
        :return:
        """
        person=Person(id,name,phone)
        self._validator.valid_person(person)
        self._repo.add_person(id,name,phone)
        undo_fun = FunctionCall(self._repo.remove_person, person.id)
        redo_fun = FunctionCall(self._repo.add_person, id,name,phone)
        o = Operation(undo_fun, redo_fun)
        self._undo.record(o)

    def remove(self,person_id):
        """
        removes a person with a given id
        :param person_id:
        :return:
        """
        persons=_filter(self.persons,lambda p : p.id == person_id)
        person=persons[0]
        self._validator.valid_id(person_id)
        self._repo.remove_person(person_id)
        undo_fun = FunctionCall(self._repo.add_person, person.id,person.name,person.phone_nr)
        redo_fun = FunctionCall(self._repo.remove_person, person_id)
        o = Operation(undo_fun, redo_fun)
        self._undo.record(o)


    def update(self,id,name,phone_nr):
        """
        updates a person s name and phone nr
        :param person:
        :return:
        """
        persons = _filter(self.persons, lambda p: p.id == id)
        ok = False
        if persons != []:
            ok = True
        if not ok:
            raise PersonRepoException("The person with the given id is not in the agenda!")
        person = persons[0]
        previous_name=person.name
        previous_number=person.phone_nr
        self._validator.valid_person(Person(id,name,phone_nr))
        self._repo.update_person(id,name,phone_nr)
        undo_fun = FunctionCall(self._repo.update_person, id,previous_name,previous_number)
        redo_fun = FunctionCall(self._repo.update_person, id,name,phone_nr)
        o = Operation(undo_fun, redo_fun)
        self._undo.record(o)

    def search_name(self,name):
        """
        searches a person by his/her name
        :param id:
        :return:
        """
        self._validator.valid_name(name)
        list=_filter(self.persons,lambda person:person.name.lower().find(name.lower())!=-1 or self._repo.get_firstname(person.name.lower())==self._repo.get_secondname(name.lower()) or self._repo.get_secondname(person.name.lower())== self._repo.get_firstname(name.lower()))
        ok = False
        if list != []:
            ok = True
        if not ok:
            raise PersonRepoException("The person with the given name is not in the agenda!")
        return list

    def search_phone(self,phone):
        """
        searches a person by his/her phone number
        :param phone:
        :return:
        """
        self._validator.valid_phonenr(phone)
        list = _filter(self.persons,
                       lambda person: person.phone_nr.find(phone)!=-1 )
        ok = False
        if list != []:
            ok = True
        if not ok:
            raise PersonRepoException("The person with the given phone number is not in the agenda!")
        return list



    def __len__(self):
        """
        Returns the length of the repository
        :return:
        """
        return len(self._repo)


