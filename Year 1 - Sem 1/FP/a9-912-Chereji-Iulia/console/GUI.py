from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import simpledialog
from service import person_service
from service import activity_service
from console.UI import UI, ActivityService, PersonService
from domain.person import PersonException
from domain.activity import ActivityException, Activity


class GUI(UI):
    def __init__(self, person_service, activity_service, undo, win):
        super().__init__(person_service, activity_service, undo)
        self._main = win
        self._main.title("Activity Planner")
        self._main.geometry('800x800')
        self._frame = Frame(cursor='arrow', width='500', height='200')

    def buttons(self):
        button1 = Button(self._main, text="List all people", fg='purple', command=self.list_ppl_gui)
        button2 = Button(self._main, text="List all activities", fg='orange', command=self.list_activities_gui)
        button3 = Button(self._main, text="Add a person", fg='purple', command = self.add_person)
        button4 = Button(self._main, text="Add an activity", fg='orange', command = self.add_activity)
        button5 = Button(self._main, text="Remove a person", fg='purple', command = self.remove_person)
        button6 = Button(self._main, text="Remove an activity", fg='orange', command = self.remove_activity)
        button7 = Button(self._main, text="Update a person", fg='purple', command = self.update_person)
        button8 = Button(self._main, text="Update an activity", fg='orange', command = self.update_activity)
        button9 = Button(self._main, text="Search for a person", fg='purple', command = self.search_person)
        button10 = Button(self._main, text="Search for an activity", fg='orange', command = self.search_activity)
        button11 = Button(self._main, text="Activities for a date", fg='blue', command = self.activs_per_day)
        button12 = Button(self._main, text="Upcoming activities with person", fg='blue', command = self.activs_with_person)
        button13 = Button(self._main, text="Upcoming busiest days", fg='blue', command = self.busiest_days)
        button14 = Button(self._main, text="Clear", fg='red', command = self.clear)
        button15 = Button(self._main, text="Undo", fg='cyan', command = self.undo)
        button16 = Button(self._main, text="Redo", fg='pink', command = self.redo)
        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()
        button5.pack()
        button6.pack()
        button7.pack()
        button8.pack()
        button9.pack()
        button10.pack()
        button11.pack()
        button12.pack()
        button13.pack()
        button14.pack()
        button15.pack()
        button16.pack()

    def list_ppl_gui(self):
        self._frame.pack()
        self.clear()
        scroll_bar = Scrollbar(self._frame)
        scroll_bar.pack(side=RIGHT, fill=Y)
        scroll_barx = Scrollbar(self._frame, orient='horizontal')
        scroll_barx.pack(side=BOTTOM, fill=X)
        mylist = Listbox(self._frame, width='500', height='200', yscrollcommand=scroll_bar.set,
                         xscrollcommand=scroll_barx.set)
        for person in self._person_service.persons:
            mylist.insert(END, str(person))
        mylist.pack()
        scroll_bar.config(command=mylist.yview)
        scroll_barx.config(command=mylist.xview)

    def list_activities_gui(self):
        self._frame.pack()
        self.clear()
        scroll_bar = Scrollbar(self._frame)
        scroll_bar.pack(side=RIGHT, fill = Y)
        scroll_barx = Scrollbar(self._frame, orient= 'horizontal')
        scroll_barx.pack(side=BOTTOM, fill = X)
        mylist = Listbox(self._frame, width='500', height='200', yscrollcommand=scroll_bar.set, xscrollcommand=scroll_barx.set)
        for activity in self._activity_service.get_all():
            mylist.insert(END, str(activity))
        mylist.pack()
        scroll_bar.config(command=mylist.yview)
        scroll_barx.config(command = mylist.xview)

    def clear(self):
        for child in self._frame.winfo_children():
            child.destroy()

    def add_person(self):
        self._frame.pack()
        id_p= int(simpledialog.askstring(title= 'ID', prompt="Enter ID:"))
        name = simpledialog.askstring(title= 'Name', prompt="Enter Name:")
        number = simpledialog.askstring(title= 'Number', prompt="Enter Number:")
        try:
            self._person_service.add(id_p,name,number)
        except PersonException as pe:
            messagebox.showerror(str(pe))

    def add_activity(self):
        self._frame.pack()
        id = int(simpledialog.askstring(title='ID', prompt="Enter ID:"))
        date = simpledialog.askstring(title='Date', prompt="Enter Date:")
        starttime = simpledialog.askstring(title='Start Time', prompt="Enter start time:")
        endtime = simpledialog.askstring(title='End Time', prompt="Enter end time:")
        description = simpledialog.askstring( title='End Description', prompt="Enter description:")
        done = False
        person_list = []
        while not done:
            person = int(simpledialog.askstring( title='Add person', prompt="Enter ID of person to do the activity with:"))
            if person == 0:
                done = True
            elif person in person_list:
                messagebox.showerror('Duplicate ID!')
            if done==False:
                person_list.append(person)

        try:
            activity=Activity(id, person_list, date, starttime, endtime, description)
            self._activity_service.add(activity)
        except ActivityException as ae:
            messagebox.showerror(str(ae))
        except ValueError as ve:
            messagebox.showerror(str(ve))

    def remove_person(self):
        self._frame.pack()
        id = simpledialog.askstring(title='ID', prompt="Enter ID:")
        id=int(id)
        try:
            self._person_service.remove(id)
        except PersonException as pe:
            messagebox.showerror(str(pe))

    def remove_activity(self):
        self._frame.pack()
        id = int(simpledialog.askstring(title='ID', prompt="Enter ID:"))
        try:
            self._activity_service.remove(id)
        except ActivityException as ae:
            messagebox.showerror(str(ae))

    def update_person(self):
        self._frame.pack()
        id = int(simpledialog.askstring(title='ID', prompt="Enter ID:"))
        name = simpledialog.askstring(title='Name', prompt="Update Name:")
        number = simpledialog.askstring(title='Number', prompt="Update Number:")
        try:
            self._person_service.update(id, name, number)
        except PersonException as pe:
            messagebox.showerror(str(pe))

    def update_activity(self):
        self._frame.pack()
        id = int(simpledialog.askstring(title='ID', prompt="Enter ID:"))
        date = simpledialog.askstring(title='Date', prompt="Update Date:")
        starttime = simpledialog.askstring(title='Start Time', prompt="Update start time:")
        endtime = simpledialog.askstring(title='End Time', prompt="Update end time:")
        description = simpledialog.askstring(title='End Description', prompt="Update description:")
        done = False
        person_list = []
        while not done:
            person = int(simpledialog.askstring(title='Add person', prompt="Update ID of person to do the activity with:"))
            if person == 0:
                done = True
            if person in person_list:
                messagebox.showerror('Duplicate ID!')
            if done==False:
                person_list.append(person)

        try:
            self._activity_service.update(id, person_list, date, starttime, endtime, description)
        except ActivityException as ae:
            messagebox.showerror(str(ae))
        except ValueError as ve:
            messagebox.showerror(str(ve))
        except AttributeError as ae:
            messagebox.showerror(str(ae))

    def search_person(self):
        self._frame.pack()
        scroll_bar = Scrollbar(self._frame)
        scroll_bar.pack(side=RIGHT, fill=Y)
        scroll_barx = Scrollbar(self._frame, orient='horizontal')
        scroll_barx.pack(side=BOTTOM, fill=X)
        mylist = Listbox(self._frame, width='500', height='200', yscrollcommand=scroll_bar.set, xscrollcommand=scroll_barx.set)
        mylist.pack()
        scroll_bar.config(command=mylist.yview)
        scroll_barx.config(command=mylist.xview)
        name_or_nr = simpledialog.askstring(title='Search', prompt="Search by name or number?")
        if name_or_nr == 'name':
            try:
                name = simpledialog.askstring(title='Search', prompt="Enter name: ").strip().lower()
                for person in self._person_service.search_name(name):
                    mylist.insert(END, str(person))
                return mylist
            except PersonException as pe:
                messagebox.showerror(str(pe))
        elif name_or_nr == 'number':
            try:
                number = simpledialog.askstring(title='Search', prompt="Enter number: ").strip().lower()
                for person in self._person_service.search_phone(number):
                    mylist.insert(END, str(person))
                return mylist
            except PersonException as pe:
                messagebox.showerror(str(pe))
        else:
            messagebox.showerror('Bad input!')

    def search_activity(self):
        self._frame.pack()
        scroll_bar = Scrollbar(self._frame)
        scroll_bar.pack(side=RIGHT, fill=Y)
        scroll_barx = Scrollbar(self._frame, orient='horizontal')
        scroll_barx.pack(side=BOTTOM, fill=X)
        mylist = Listbox(self._frame, width='500', height='200', yscrollcommand=scroll_bar.set,
                         xscrollcommand=scroll_barx.set)
        mylist.pack()
        scroll_bar.config(command=mylist.yview)
        scroll_barx.config(command=mylist.xview)
        dt_or_dscr = simpledialog.askstring(title='Search', prompt="Search by date and time or description?")
        if dt_or_dscr == 'date and time':
            try:
                date = simpledialog.askstring(title='Search', prompt="Enter date: ").strip().lower()
                starttime = simpledialog.askstring(title='Search', prompt="Enter start time: ").strip().lower()
                for activity in self._activity_service.search_date_time(date, starttime):
                    mylist.insert(END, str(activity))
                return mylist
            except ActivityException as ae:
                messagebox.showerror(str(ae))

        elif dt_or_dscr == 'description':
            try:
                descr = simpledialog.askstring(title='Search', prompt="Enter description: ").strip().lower()
                for activity in self._activity_service.search_description(descr):
                    mylist.insert(END, str(activity))
                return mylist
            except ActivityException as ae:
                messagebox.showerror(str(ae))

        else:
            messagebox.showerror('Bad input!')

    def activs_per_day(self):
        scroll_bar = Scrollbar(self._frame)
        scroll_bar.pack(side=RIGHT, fill=Y)
        scroll_barx = Scrollbar(self._frame, orient='horizontal')
        scroll_barx.pack(side=BOTTOM, fill=X)
        mylist = Listbox(self._frame, width='500', height='200', yscrollcommand=scroll_bar.set,
                         xscrollcommand=scroll_barx.set)
        mylist.pack()
        scroll_bar.config(command=mylist.yview)
        scroll_barx.config(command=mylist.xview)
        self._frame.pack()
        date = simpledialog.askstring(title='Statistics', prompt="Enter date: ").strip().lower()
        for activity in self._activity_service.st_activities_for_a_date(date):
            mylist.insert(END, str(activity))
        return mylist



    def activs_with_person(self):
        scroll_bar = Scrollbar(self._frame)
        scroll_bar.pack(side=RIGHT, fill=Y)
        scroll_barx = Scrollbar(self._frame, orient='horizontal')
        scroll_barx.pack(side=BOTTOM, fill=X)
        mylist = Listbox(self._frame, width='500', height='200', yscrollcommand=scroll_bar.set,
                         xscrollcommand=scroll_barx.set)
        mylist.pack()
        scroll_bar.config(command=mylist.yview)
        scroll_barx.config(command=mylist.xview)
        self._frame.pack()
        id = int(simpledialog.askstring(title='Statistics', prompt="Enter ID of the person: ").strip().lower())
        for activity in self._activity_service.st_activities_with_a_person(id):
            mylist.insert(END, str(activity))
        #self.list_act_person(id)
        return mylist

    def busiest_days(self):
        scroll_bar = Scrollbar(self._frame)
        scroll_bar.pack(side=RIGHT, fill=Y)
        scroll_barx = Scrollbar(self._frame, orient='horizontal')
        scroll_barx.pack(side=BOTTOM, fill=X)
        mylist = Listbox(self._frame, width='500', height='200', yscrollcommand=scroll_bar.set,
                         xscrollcommand=scroll_barx.set)
        mylist.pack()
        scroll_bar.config(command=mylist.yview)
        scroll_barx.config(command=mylist.xview)
        self._frame.pack()
        for activity_list in self._activity_service.st_busiest_days():
            mylist.insert(END, str(activity_list))
        return mylist

    def undo(self):
        try:
            self._undo.undo()
        except ValueError:
            messagebox.showerror("No more undos")

    def redo(self):
        try:
            self._undo.redo()
        except ValueError:
            messagebox.showerror("No more redos")

