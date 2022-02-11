from console.GUI import GUI
from console.UI import UI
from domain.activity import ActivityValidator, Activity
from domain.person import PersonValidator, Person
import random
from datetime import date
from tkinter import *

from repository import PersonTextRepo
from repository.ActivityBinaryRepo import ActivityBinaryRepo
from repository.ActivityDatabaseRepo import DatabaseActivityRepo
from repository.ActivityJsonRepo import ActivityJsonRepo
from repository.ActivityTextRepo import ActivityTextFileRepository
from repository.PersonBinaryRepo import PersonBinaryRepo
from repository.PersonJsonRepo import PersonJsonRepo
from repository.PersonRepoDatabase import DatabasePeopleRepo
from repository.PersonTextRepo import PersonTextFileRepository
from start.Settings import Settings

from repository.activity_repo import ActivityRepo
from repository.person_repo import PersonRepo
from repository.undo_service import Undo
from service.activity_service import ActivityService
from service.person_service import PersonService
from repository import ActivityTextRepo


def create_persons_list():
    persons = []
    firstname_list = ['Maria', 'Alex', 'Iulia', 'Oana', 'Mihai', 'Ioana', 'Gabriela',
                'Patrick', 'Anca', 'Serban', 'Carmen', 'Florin', 'George', 'Andrei', 'Mihnea']

    surname_list = ['Chereji', 'Olariu', 'Pop', 'Pustai', 'Micle', 'Opris', 'Stan', 'Tomsa', 'Feldi',
               'Ripan', 'Opre', 'Ardelean', 'Micu', 'Magureanu', 'Roman', 'Culic']
    persons_ids = []
    for i in range(1, 11):
        persons_ids.append(i)

    for i in range(10):
        id = random.choice(persons_ids)
        persons_ids.remove(id)
        firstname = random.choice(firstname_list)
        surname = random.choice(surname_list)
        name = firstname + ' ' + surname
        phone_number = '0'
        for i in range(9):
            digit = random.randint(0, 9)
            phone_number += str(digit)
        persons.append(Person(id, name, phone_number))
    return persons


def create_activity_list():
    activity = []
    possible_activities = ["cooking", "dance classes", "sleeping", "going for a walk", "learning", "going out",
                         "online classes", "shopping", "eating", "visiting a friend", "reading", "watching a movie",
                         "meeting", "sport"]
    activity_ids = []
    for i in range(1, 11):
        activity_ids.append(i)
    for i in range(10):
        id_act = random.choice(activity_ids)
        activity_ids.remove(id_act)
        person_list = []
        for j in range(1, 6):
            persons_id = random.randint(1, 10)
            ok = 0
            for t in person_list:
                if t == persons_id:
                    ok = 1
            if ok == 0:
                person_list.append(persons_id)
        start_date = date.today().replace(day=1, month=1).toordinal()
        end_date = date.today().replace(year=2021).toordinal()
        date_act = date.fromordinal(random.randint(start_date, end_date))
        hour = random.randint(0, 22)
        chour=hour
        if hour<10:
            hour='0'+str(hour)
        minutes = random.randint(0, 58)
        cmin=minutes
        if minutes < 10:
            minutes='0'+str(minutes)
        start_time = str(hour)+":"+str(minutes)
        hour1 = random.randint(chour, 23)
        if hour1 < 10:
            hour1 = '0' + str(hour1)
        minutes1 = random.randint(cmin, 59)
        if minutes1 < 10:
            minutes1 = '0' + str(minutes1)
        end_time = str(hour1) + ":" + str(minutes1)
        description = random.choice(possible_activities)
        activity.append(Activity(id_act, person_list, str(date_act), start_time,end_time, description))
    return activity


settings = Settings()
person_validator = PersonValidator()
activity_validator = ActivityValidator()
undo = Undo()

if settings.typeofrepo == 'inmemory':
    person_repo = PersonRepo(create_persons_list())
    person_service = PersonService(person_repo, person_validator, undo)
    activity_repo = ActivityRepo(create_activity_list())
    activity_service = ActivityService(activity_repo, activity_validator, undo, person_repo)
elif settings.typeofrepo =="text file":
    p_repo= PersonTextFileRepository(settings.person_repo)
    activity_repo = ActivityTextFileRepository(settings.activity_repo)
    person_service = PersonService(p_repo, person_validator, undo)
    activity_service = ActivityService(activity_repo, activity_validator, undo, p_repo)
elif settings.typeofrepo == "binary file":
    person_repo = PersonBinaryRepo(settings.person_repo)
    activity_repo = ActivityBinaryRepo(settings.activity_repo)
    person_service = PersonService(person_repo, person_validator, undo)
    activity_service = ActivityService(activity_repo, activity_validator,undo,person_repo)
elif settings.typeofrepo == 'json file':
    person_repo = PersonJsonRepo(settings.person_repo)
    activity_repo = ActivityJsonRepo(settings.activity_repo)
    person_service = PersonService(person_repo, person_validator, undo)
    activity_service = ActivityService(activity_repo, activity_validator, undo, person_repo)
elif settings.typeofrepo == 'data base':
    person_repo = DatabasePeopleRepo(settings.person_repo)
    activity_repo = DatabaseActivityRepo(settings.activity_repo)
    person_service = PersonService(person_repo, person_validator, undo)
    activity_service = ActivityService(activity_repo, activity_validator, undo, person_repo)


if settings.menu == 'gui':
    window=Tk()
    gui=GUI(person_service, activity_service, undo, window)
    gui.buttons()
    window.mainloop()
elif settings.menu == "ui":
    ui = UI(person_service, activity_service, undo)
    ui.start_ui()
