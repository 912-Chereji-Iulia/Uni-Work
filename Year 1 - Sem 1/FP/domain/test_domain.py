import unittest
from domain.person import Person, PersonValidationException, PersonException, PersonValidator
from domain.activity import Activity, ActivityValidator, ActivityException, ActivityExceptionValidator


class PersonTest(unittest.TestCase):
    def test_person(self):
        person=Person(1,"Chereji Iulia",'0721389973')
        self.assertEqual(person.id,1)
        self.assertEqual(person.name,"Chereji Iulia")
        self.assertEqual(person.phone_nr,'0721389973')
        self.assertEqual(str(person),' id: 1  name: Chereji Iulia  phone number: 0721389973')

    def test_pers_validator(self):
        person = Person(0, '', "0721")
        valid_person = PersonValidator()
        self.assertRaises(PersonValidationException,valid_person.valid_person,person)

        person1=Person(0,"Chereji Iulia","0712345678")
        self.assertRaises(PersonValidationException, valid_person.valid_person, person1)

        person2 = Person(1, '23' , "0712345678")
        self.assertRaises(PersonValidationException, valid_person.valid_person, person2)

        person3 = Person(2, "Chereji Iulia", '23' )
        self.assertRaises(PersonValidationException, valid_person.valid_person, person3)

        person4 = Person(0, "", "0712345678")
        self.assertRaises(PersonValidationException, valid_person.valid_person, person4)

        person5 = Person(0, "Chereji Iulia", "")
        self.assertRaises(PersonValidationException, valid_person.valid_person, person5)

        person6 = Person(6, "23", "071")
        self.assertRaises(PersonValidationException, valid_person.valid_person, person6)

        person7 = Person(1, "Chereji Iulia", "0712389973")
        valid_person.valid_person(person7)

    def test_person_valid(self):
        valid_person = PersonValidator()
        try:

            self.assertFalse(valid_person(Person('a',"Iulia Pop",'0721389973')))
        except PersonException:
            assert True

        try:
            self.assertFalse(valid_person(Person(1,23,'0721389973')))
        except PersonException:
            assert True

        try:
            self.assertFalse(valid_person(Person(1,"Iulia Pop",23)))
        except PersonException:
            assert True


    def test_validator(self):
        error=["Invalid phone number for person"]
        pve=PersonValidationException(error)
        self.assertEqual(str(pve),"Invalid phone number for person\n")





class ActivityTest(unittest.TestCase):
    def test_activity(self):
        activity= Activity(1,[1,2],'2020-08-02','20:20','20:50','sport')
        self.assertEqual(activity.activity_id,1)
        self.assertEqual(activity.person_ids,[1,2])
        self.assertEqual(activity.date,'2020-08-02')
        self.assertEqual(activity.start_time, '20:20')
        self.assertEqual(activity.end_time, '20:50')
        self.assertEqual(activity.description, 'sport')
        self.assertEqual(str(activity),' activity id: 1 persons ids: [1, 2]  date: 2020-08-02  start time: 20:20  end time: 20:50  description: sport')

    def test_activity_validator(self):
        activity = Activity(0,[3],"2020-32-21", "10", "12", "")
        valid_activity = ActivityValidator()
        self.assertRaises(ActivityExceptionValidator, valid_activity.valid_activity, activity)

        activity2 = Activity(0,[1,2], "2020-11-10", "08:00", "08:30", "eating")
        self.assertRaises(ActivityExceptionValidator, valid_activity.valid_activity, activity2)

        activity3 = Activity(1,[1,2], "2020-32-21", "08:00", "08:30", "eating")
        self.assertRaises(ActivityExceptionValidator, valid_activity.valid_activity, activity3)

        activity4 = Activity(1,[1,2], "2020-11-10", "24:30", "08:30", "food")
        self.assertRaises(ActivityExceptionValidator, valid_activity.valid_activity, activity4)

        activity5 = Activity(1,[1,2], "2020-11-10", "08:00", "23:65", "food")
        self.assertRaises(ActivityExceptionValidator, valid_activity.valid_activity, activity5)

        activity6 = Activity(1,[1,2], "2020-11-10", "08:60", "08:30", "eating")
        self.assertRaises(ActivityExceptionValidator, valid_activity.valid_activity, activity6)

        activity7 = Activity(0,[1,2], "2020", "08:00", "08:30", "food")
        self.assertRaises(ActivityExceptionValidator, valid_activity.valid_activity, activity7)

        activity8 = Activity(0,[1,2], "2020-11-10", "08:60", "08:30", "food")
        self.assertRaises(ActivityExceptionValidator, valid_activity.valid_activity, activity8)

        activity9 = Activity(0,[1,2], "2020-11-10", "08:00", "07:20", "food")
        self.assertRaises(ActivityExceptionValidator, valid_activity.valid_activity, activity9)

        activity10 = Activity(0,[1,2], "2020-11-10", "08:00", "08:30", "")
        self.assertRaises(ActivityExceptionValidator, valid_activity.valid_activity, activity10)

        activity11 = Activity(1,[1,2], "2020", "24:60", "08:30", "food")
        self.assertRaises(ActivityExceptionValidator, valid_activity.valid_activity, activity11)

        activity12 = Activity(1,[1,2], "2020", "08:00", "24:50", "food")
        self.assertRaises(ActivityExceptionValidator, valid_activity.valid_activity, activity12)

        activity13 = Activity(1,[1,2], "2020", "08:00", "08:30", "eating")
        self.assertRaises(ActivityExceptionValidator, valid_activity.valid_activity, activity13)

        activity14 = Activity(1,[1,2], "2020-11-10", "00:60", "01:56", "food")
        self.assertRaises(ActivityExceptionValidator, valid_activity.valid_activity, activity14)

        activity15 = Activity(1,[1,2], "2020-11-10", "00:60", "08:30", "food")
        self.assertRaises(ActivityExceptionValidator, valid_activity.valid_activity, activity15)

        activity16 = Activity(1,[1,2], "2020-11-10", "08:00", "24:60", "eating")
        self.assertRaises(ActivityExceptionValidator, valid_activity.valid_activity, activity16)

        activity18 = Activity(1, [1, 2], "2020-02-30", "08:00", "24:60", "eating")
        self.assertRaises(ActivityExceptionValidator, valid_activity.valid_activity, activity18)

        activity19 = Activity(1, [1, 2], "2020-11-100", "08:00", "24:60", "eating")
        self.assertRaises(ActivityExceptionValidator, valid_activity.valid_activity, activity19)

        activity20 = Activity(1, [1, 2], "2020-01-32", "08:00", "24:60", "eating")
        self.assertRaises(ActivityExceptionValidator, valid_activity.valid_activity, activity20)

        activity17 = Activity(1,[1,2], "2020-11-10", "08:00", "08:30", "food")
        valid_activity.valid_activity(activity17)

    def test_validator(self):
        error=["Invalid activity id!"]
        ave=ActivityExceptionValidator(error)
        self.assertEqual(str(ave),"Invalid activity id!\n")



    def test_act_valid(self):
        valid_activity = ActivityValidator()
        try:

            self.assertFalse(valid_activity(Activity("a",[1,2],"2020-12-20","08:02","08:30","sport")))
        except ActivityException:
            assert True


        try:
            self.assertFalse(valid_activity(Activity(1, ['1', 2], "2020-12-20", "08:02", "08:30", "sport")))
        except ActivityException:
            assert True


        try:

            self.assertFalse(valid_activity(Activity(1, [1, 2], 20, "08:02", "08:30", "sport")))
        except ActivityException:
            assert True

        try:

            self.assertFalse(valid_activity(Activity(1, [1, 2], "2020-12-20", 8, "08:30", "sport")))
        except ActivityException:
            assert True

        try:

            self.assertFalse(valid_activity(Activity(1, [1, 2], "2020-12-20",'08:02', 8,  "sport")))
        except ActivityException:
            assert True

        try:

            self.assertFalse(valid_activity(Activity(1, [1, 2], "2020-12-20", "08:02", "08:30", 23)))
        except ActivityException:
            assert True




