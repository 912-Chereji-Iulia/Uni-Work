from tkinter import *
from tkinter import messagebox

from strategy.Strategy import Strategy


class BoardGUI(Frame):
    def __init__(self, parent, controller, game:Strategy):
        Frame.__init__(self, parent)
        self._game = game
        self.__ctr = controller
        self.turn = 1
        self.reset = 0
        self.first = 0

        self.Button1 = Button(self, activebackground="#d9d9d9", activeforeground="#000000", background="#ffffff",
                              disabledforeground="#a3a3a3", foreground="#000000", highlightcolor="black", relief=SUNKEN,
                              height=2, width=5, pady="0", padx="0",
                              command=lambda: self.make_move(0, 0, self.Button1, self.Button2, self.Button8, self.Button7))
        self.Button1.grid(row=1, column=0)

        self.Button2 = Button(self, activebackground="#d9d9d9", activeforeground="#000000", background="#ffffff",
                              disabledforeground="#a3a3a3", foreground="#000000", highlightcolor="black", relief=SUNKEN,
                              height=2, width=5, pady="0", padx="0",
                              command=lambda: self.make_move(0, 1, self.Button2, self.Button1, self.Button3,
                                                             self.Button7, self.Button8, self.Button9))
        self.Button2.grid(row=1, column=1)

        self.Button3 = Button(self, activebackground="#d9d9d9", activeforeground="#000000", background="#ffffff",
                              disabledforeground="#a3a3a3", foreground="#000000", highlightcolor="black", relief=SUNKEN,
                              height=2, width=5, pady="0", padx="0",
                              command=lambda: self.make_move(0, 2, self.Button3, self.Button2, self.Button8,
                                                             self.Button4, self.Button9, self.Button10))
        self.Button3.grid(row=1, column=2)

        self.Button4 = Button(self, activebackground="#d9d9d9", activeforeground="#000000", background="#ffffff",
                              disabledforeground="#a3a3a3", foreground="#000000", highlightcolor="black", relief=SUNKEN,
                              height=2, width=5, pady="0", padx="0",
                              command=lambda: self.make_move(0, 3, self.Button4, self.Button5, self.Button3,
                                                             self.Button9, self.Button10, self.Button11))
        self.Button4.grid(row=1, column=3)

        self.Button5 = Button(self, activebackground="#d9d9d9", activeforeground="#000000", background="#ffffff",
                              disabledforeground="#a3a3a3", foreground="#000000", highlightcolor="black", relief=SUNKEN,
                              height=2, width=5, pady="0", padx="0",
                              command=lambda: self.make_move(0, 4, self.Button5, self.Button6, self.Button10,
                                                             self.Button4, self.Button11, self.Button12))
        self.Button5.grid(row=1, column=4)

        self.Button6 = Button(self, activebackground="#d9d9d9", activeforeground="#000000", background="#ffffff",
                              disabledforeground="#a3a3a3", foreground="#000000", highlightcolor="black", relief=SUNKEN,
                              height=2, width=5, pady="0", padx="0",
                              command=lambda: self.make_move(0, 5, self.Button6, self.Button5, self.Button11,
                                                             self.Button12))
        self.Button6.grid(row=1, column=5)

        self.Button7 = Button(self, activebackground="#d9d9d9", activeforeground="#000000", background="#ffffff",
                              disabledforeground="#a3a3a3", foreground="#000000", highlightcolor="black", relief=SUNKEN,
                              height=2, width=5, pady="0", padx="0",
                              command=lambda: self.make_move(1, 0, self.Button7, self.Button1, self.Button2,
                                                             self.Button8, self.Button13, self.Button14))
        self.Button7.grid(row=2, column=0)

        self.Button8 = Button(self, activebackground="#d9d9d9", activeforeground="#000000", background="#ffffff",
                              disabledforeground="#a3a3a3", foreground="#000000", highlightcolor="black", relief=SUNKEN,
                              height=2, width=5, pady="0", padx="0",
                              command=lambda: self.make_move(1, 1, self.Button8, self.Button1, self.Button3,
                                                             self.Button7, self.Button2, self.Button9,
                                                             self.Button13, self.Button14, self.Button15))
        self.Button8.grid(row=2, column=1)

        self.Button9 = Button(self, activebackground="#d9d9d9", activeforeground="#000000", background="#ffffff",
                              disabledforeground="#a3a3a3", foreground="#000000", highlightcolor="black", relief=SUNKEN,
                              height=2, width=5, pady="0", padx="0",
                              command=lambda: self.make_move(1, 2, self.Button9, self.Button2, self.Button8,
                                                             self.Button4, self.Button3, self.Button10,
                                                             self.Button16, self.Button14, self.Button15))
        self.Button9.grid(row=2, column=2)

        self.Button10 = Button(self, activebackground="#d9d9d9", activeforeground="#000000", background="#ffffff",
                              disabledforeground="#a3a3a3", foreground="#000000", highlightcolor="black", relief=SUNKEN,
                              height=2, width=5, pady="0", padx="0",
                              command=lambda: self.make_move(1, 3, self.Button10, self.Button5, self.Button3,
                                                             self.Button9, self.Button4, self.Button11,
                                                             self.Button16, self.Button17, self.Button15))
        self.Button10.grid(row=2, column=3)

        self.Button11 = Button(self, activebackground="#d9d9d9", activeforeground="#000000", background="#ffffff",
                              disabledforeground="#a3a3a3", foreground="#000000", highlightcolor="black", relief=SUNKEN,
                              height=2, width=5, pady="0", padx="0",
                              command=lambda: self.make_move(1, 4, self.Button11, self.Button6, self.Button10,
                                                             self.Button4, self.Button5, self.Button12,
                                                             self.Button16, self.Button17, self.Button18))
        self.Button11.grid(row=2, column=4)

        self.Button12 = Button(self, activebackground="#d9d9d9", activeforeground="#000000", background="#ffffff",
                              disabledforeground="#a3a3a3", foreground="#000000", highlightcolor="black", relief=SUNKEN,
                              height=2, width=5, pady="0", padx="0",
                              command=lambda: self.make_move(1, 5, self.Button12, self.Button5, self.Button11,
                                                             self.Button6, self.Button17, self.Button18))
        self.Button12.grid(row=2, column=5)

        self.Button13 = Button(self, activebackground="#d9d9d9", activeforeground="#000000", background="#ffffff",
                              disabledforeground="#a3a3a3", foreground="#000000", highlightcolor="black", relief=SUNKEN,
                              height=2, width=5, pady="0", padx="0",
                              command=lambda: self.make_move(2, 0, self.Button13, self.Button19, self.Button20,
                                                             self.Button8, self.Button7, self.Button14))
        self.Button13.grid(row=3, column=0)

        self.Button14 = Button(self, activebackground="#d9d9d9", activeforeground="#000000", background="#ffffff",
                              disabledforeground="#a3a3a3", foreground="#000000", highlightcolor="black", relief=SUNKEN,
                              height=2, width=5, pady="0", padx="0",
                              command=lambda: self.make_move(2, 1, self.Button14, self.Button19, self.Button21,
                                                             self.Button7, self.Button20, self.Button9,
                                                             self.Button13, self.Button8, self.Button15))
        self.Button14.grid(row=3, column=1)

        self.Button15 = Button(self, activebackground="#d9d9d9", activeforeground="#000000", background="#ffffff",
                              disabledforeground="#a3a3a3", foreground="#000000", highlightcolor="black", relief=SUNKEN,
                              height=2, width=5, pady="0", padx="0",
                              command=lambda: self.make_move(2, 2, self.Button15, self.Button20, self.Button8,
                                                             self.Button21, self.Button22, self.Button10,
                                                             self.Button16, self.Button14, self.Button9))
        self.Button15.grid(row=3, column=2)

        self.Button16 = Button(self, activebackground="#d9d9d9", activeforeground="#000000", background="#ffffff",
                               disabledforeground="#a3a3a3", foreground="#000000", highlightcolor="black",
                               relief=SUNKEN,
                               height=2, width=5, pady="0", padx="0",
                               command=lambda: self.make_move(2, 3, self.Button16, self.Button21, self.Button22,
                                                              self.Button9, self.Button23, self.Button11,
                                                              self.Button10, self.Button17, self.Button15))
        self.Button16.grid(row=3, column=3)

        self.Button17 = Button(self, activebackground="#d9d9d9", activeforeground="#000000", background="#ffffff",
                               disabledforeground="#a3a3a3", foreground="#000000", highlightcolor="black",
                               relief=SUNKEN,
                               height=2, width=5, pady="0", padx="0",
                               command=lambda: self.make_move(2, 4, self.Button17, self.Button22, self.Button10,
                                                              self.Button24, self.Button23, self.Button12,
                                                              self.Button16, self.Button11, self.Button18))
        self.Button17.grid(row=3, column=4)

        self.Button18 = Button(self, activebackground="#d9d9d9", activeforeground="#000000", background="#ffffff",
                               disabledforeground="#a3a3a3", foreground="#000000", highlightcolor="black",
                               relief=SUNKEN,
                               height=2, width=5, pady="0", padx="0",
                               command=lambda: self.make_move(2, 5, self.Button18, self.Button23, self.Button11,
                                                              self.Button24, self.Button17, self.Button12))
        self.Button18.grid(row=3, column=5)

        self.Button19 = Button(self, activebackground="#d9d9d9", activeforeground="#000000", background="#ffffff",
                               disabledforeground="#a3a3a3", foreground="#000000", highlightcolor="black",
                               relief=SUNKEN,
                               height=2, width=5, pady="0", padx="0",
                               command=lambda: self.make_move(3, 0, self.Button19, self.Button13, self.Button20,
                                                              self.Button25, self.Button26, self.Button14))
        self.Button19.grid(row=4, column=0)

        self.Button20 = Button(self, activebackground="#d9d9d9", activeforeground="#000000", background="#ffffff",
                               disabledforeground="#a3a3a3", foreground="#000000", highlightcolor="black",
                               relief=SUNKEN,
                               height=2, width=5, pady="0", padx="0",
                               command=lambda: self.make_move(3, 1, self.Button20, self.Button19, self.Button21,
                                                              self.Button25, self.Button14, self.Button26,
                                                              self.Button13, self.Button27, self.Button15))
        self.Button20.grid(row=4, column=1)

        self.Button21 = Button(self, activebackground="#d9d9d9", activeforeground="#000000", background="#ffffff",
                               disabledforeground="#a3a3a3", foreground="#000000", highlightcolor="black",
                               relief=SUNKEN,
                               height=2, width=5, pady="0", padx="0",
                               command=lambda: self.make_move(3, 2, self.Button21, self.Button20, self.Button26,
                                                              self.Button15, self.Button22, self.Button28,
                                                              self.Button16, self.Button14, self.Button27))
        self.Button21.grid(row=4, column=2)

        self.Button22 = Button(self, activebackground="#d9d9d9", activeforeground="#000000", background="#ffffff",
                               disabledforeground="#a3a3a3", foreground="#000000", highlightcolor="black",
                               relief=SUNKEN,
                               height=2, width=5, pady="0", padx="0",
                               command=lambda: self.make_move(3, 3, self.Button22, self.Button21, self.Button16,
                                                              self.Button27, self.Button23, self.Button29,
                                                              self.Button28, self.Button17, self.Button15))
        self.Button22.grid(row=4, column=3)

        self.Button23 = Button(self, activebackground="#d9d9d9", activeforeground="#000000", background="#ffffff",
                               disabledforeground="#a3a3a3", foreground="#000000", highlightcolor="black",
                               relief=SUNKEN,
                               height=2, width=5, pady="0", padx="0",
                               command=lambda: self.make_move(3, 4, self.Button23, self.Button22, self.Button28,
                                                              self.Button24, self.Button17, self.Button30,
                                                              self.Button16, self.Button29, self.Button18))
        self.Button23.grid(row=4, column=4)

        self.Button24 = Button(self, activebackground="#d9d9d9", activeforeground="#000000", background="#ffffff",
                               disabledforeground="#a3a3a3", foreground="#000000", highlightcolor="black",
                               relief=SUNKEN,
                               height=2, width=5, pady="0", padx="0",
                               command=lambda: self.make_move(3, 5, self.Button24, self.Button23, self.Button29,
                                                              self.Button18, self.Button17, self.Button30))
        self.Button24.grid(row=4, column=5)

        self.Button25 = Button(self, activebackground="#d9d9d9", activeforeground="#000000", background="#ffffff",
                               disabledforeground="#a3a3a3", foreground="#000000", highlightcolor="black",
                               relief=SUNKEN,
                               height=2, width=5, pady="0", padx="0",
                               command=lambda: self.make_move(4, 0, self.Button25, self.Button31, self.Button32,
                                                              self.Button19, self.Button26, self.Button20))
        self.Button25.grid(row=5, column=0)

        self.Button26 = Button(self, activebackground="#d9d9d9", activeforeground="#000000", background="#ffffff",
                               disabledforeground="#a3a3a3", foreground="#000000", highlightcolor="black",
                               relief=SUNKEN,
                               height=2, width=5, pady="0", padx="0",
                               command=lambda: self.make_move(4, 1, self.Button26, self.Button19, self.Button21,
                                                              self.Button25, self.Button32, self.Button20,
                                                     self.Button31, self.Button27, self.Button33))
        self.Button26.grid(row=5, column=1)

        self.Button27 = Button(self, activebackground="#d9d9d9", activeforeground="#000000", background="#ffffff",
                               disabledforeground="#a3a3a3", foreground="#000000", highlightcolor="black",
                               relief=SUNKEN,
                               height=2, width=5, pady="0", padx="0",
                               command=lambda: self.make_move(4, 2, self.Button27, self.Button20, self.Button26,
                                                              self.Button34, self.Button22, self.Button28,
                                                              self.Button33, self.Button32, self.Button21))
        self.Button27.grid(row=5, column=2)

        self.Button28 = Button(self, activebackground="#d9d9d9", activeforeground="#000000", background="#ffffff",
                               disabledforeground="#a3a3a3", foreground="#000000", highlightcolor="black",
                               relief=SUNKEN,
                               height=2, width=5, pady="0", padx="0",
                               command=lambda: self.make_move(4, 3, self.Button28, self.Button21, self.Button33,
                                                              self.Button27, self.Button23, self.Button29,
                                                              self.Button22, self.Button35, self.Button34))
        self.Button28.grid(row=5, column=3)

        self.Button29 = Button(self, activebackground="#d9d9d9", activeforeground="#000000", background="#ffffff",
                               disabledforeground="#a3a3a3", foreground="#000000", highlightcolor="black",
                               relief=SUNKEN,
                               height=2, width=5, pady="0", padx="0",
                               command=lambda: self.make_move(4, 4, self.Button29, self.Button22, self.Button28,
                                                              self.Button24, self.Button36, self.Button30,
                                                              self.Button35, self.Button23, self.Button34))
        self.Button29.grid(row=5, column=4)

        self.Button30 = Button(self, activebackground="#d9d9d9", activeforeground="#000000", background="#ffffff",
                               disabledforeground="#a3a3a3", foreground="#000000", highlightcolor="black",
                               relief=SUNKEN,
                               height=2, width=5, pady="0", padx="0",
                               command=lambda: self.make_move(4, 5, self.Button30, self.Button23, self.Button29,
                                                              self.Button35, self.Button36, self.Button24))
        self.Button30.grid(row=5, column=5)

        self.Button31 = Button(self, activebackground="#d9d9d9", activeforeground="#000000", background="#ffffff",
                               disabledforeground="#a3a3a3", foreground="#000000", highlightcolor="black",
                               relief=SUNKEN,
                               height=2, width=5, pady="0", padx="0",
                               command=lambda: self.make_move(5, 0, self.Button31, self.Button25, self.Button32,
                                                              self.Button26))
        self.Button31.grid(row=6, column=0)

        self.Button32 = Button(self, activebackground="#d9d9d9", activeforeground="#000000", background="#ffffff",
                               disabledforeground="#a3a3a3", foreground="#000000", highlightcolor="black",
                               relief=SUNKEN,
                               height=2, width=5, pady="0", padx="0",
                               command=lambda: self.make_move(5, 1, self.Button32,
                                                              self.Button25, self.Button26,
                                                              self.Button31, self.Button27, self.Button33))
        self.Button32.grid(row=6, column=1)

        self.Button33 = Button(self, activebackground="#d9d9d9", activeforeground="#000000", background="#ffffff",
                               disabledforeground="#a3a3a3", foreground="#000000", highlightcolor="black",
                               relief=SUNKEN,
                               height=2, width=5, pady="0", padx="0",
                               command=lambda: self.make_move(5, 2, self.Button33,  self.Button26,
                                                              self.Button34,  self.Button28,
                                                              self.Button27, self.Button32))
        self.Button33.grid(row=6, column=2)

        self.Button34 = Button(self, activebackground="#d9d9d9", activeforeground="#000000", background="#ffffff",
                               disabledforeground="#a3a3a3", foreground="#000000", highlightcolor="black",
                               relief=SUNKEN,
                               height=2, width=5, pady="0", padx="0",
                               command=lambda: self.make_move(5, 3, self.Button34, self.Button33,
                                                              self.Button27, self.Button29,
                                                               self.Button35, self.Button28))
        self.Button34.grid(row=6, column=3)

        self.Button35 = Button(self, activebackground="#d9d9d9", activeforeground="#000000", background="#ffffff",
                               disabledforeground="#a3a3a3", foreground="#000000", highlightcolor="black",
                               relief=SUNKEN,
                               height=2, width=5, pady="0", padx="0",
                               command=lambda: self.make_move(5, 4, self.Button35, self.Button28,
                                                                self.Button36, self.Button30,
                                                              self.Button29, self.Button34))
        self.Button35.grid(row=6, column=4)

        self.Button36 = Button(self, activebackground="#d9d9d9", activeforeground="#000000", background="#ffffff",
                               disabledforeground="#a3a3a3", foreground="#000000", highlightcolor="black",
                               relief=SUNKEN,
                               height=2, width=5, pady="0", padx="0",
                               command=lambda: self.make_move(5, 5, self.Button36, self.Button29,
                                                              self.Button35, self.Button30))
        self.Button36.grid(row=6, column=5)

        self.button_array = {}
        iterate = 0
        for button in (self.Button1, self.Button2, self.Button3, self.Button4, self.Button5, self.Button6, self.Button7,
                    self.Button8, self.Button9, self.Button10, self.Button11, self.Button12, self.Button13, self.Button14,
                    self.Button15, self.Button16, self.Button17, self.Button18, self.Button19, self.Button20,
                    self.Button21, self.Button22, self.Button23, self.Button24, self.Button25, self.Button26,
                    self.Button27, self.Button28, self.Button29, self.Button30, self.Button31, self.Button32,
                    self.Button33, self.Button34, self.Button35, self.Button36):
            self.button_array[iterate] = button
            iterate += 1


        info = Label(self, font=('terminal', 20, 'italic'), text="6x6 Board", anchor='w')
        info.grid(row=0, column=7)
        self.ButtonQuit = Button(self, background="#DA2C43", text="Quit", height=2, width=5,
                                 command=lambda: self.quit())
        self.ButtonQuit.grid(row=2, column=8)
        self.ButtonReset = Button(self, background="light green", text="Reset", height=2, width=5,
                                  command=lambda: self.reset_game())
        self.ButtonReset.grid(row=2, column=7)

    def create_board(self):
        self._game.set_row(6)
        self._game.set_column(6)
        self._game.create_board()

    def quit(self):
        self.reset = 1
        self.ButtonReset.invoke()
        self.__ctr.quit_frame()

    def make_move(self, x, y, *buttons):
        try:
            if self.turn == 1:
                self._game.player_move(x, y)
                for button in buttons:
                    button.configure(bg="#B2BEB5")
                buttons[0].configure(text="0", fg="orange", bg="white")
                if self._game.game_not_over() is False:
                    messagebox.showinfo("Congrats!", "You won!")
                    return
                self.turn = 2
                point = self._game.computer_move(self.first, x, y)
                index = point.get_row() * 6 + point.get_column()
                self.button_array[index].invoke()
            if self.turn == 2:
                for button in buttons:
                    button.configure(bg="#B2BEB5")
                buttons[0].configure(text="X", fg="purple", bg="white")
                self.turn = 1
                if self._game.game_not_over() is False:
                    messagebox.showinfo("Try again!", "Computer has won!")
                    return
        except Exception as error:
            messagebox.showinfo("Error", "Invalid move: " + str(error))

    def first_ai(self):
        self.turn = 2
        self.first = 1
        point = self._game.computer_move(self.first, 0, 0)
        index = point.get_row() * 6 + point.get_column()
        self.button_array[index].invoke()

    def reset_game(self):
        if self.reset == 1:
            self._game.reset_board()
            self.reset = 0
            self.first = 0
            for x in range(0, 36):
                self.button_array[x].configure(text='', bg="white")
        else:
            self._game.reset_board()
            self._game.set_row(6)
            self._game.set_column(6)
            self._game.create_board()
            self.turn = 1
            for x in range(0, 36):
                self.button_array[x].configure(text='', bg="white")
            if self.first == 1:
                self.first_ai()