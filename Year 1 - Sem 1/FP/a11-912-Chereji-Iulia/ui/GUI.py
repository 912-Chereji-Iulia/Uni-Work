from tkinter import *
from tkinter import messagebox
from domain.board_gui import BoardGUI

class StartGame(Frame):
    def __init__(self, parent, controller, strategy):
        Frame.__init__(self, parent)
        self.game = ""
        self._controller = controller

        title = Label(self, font=('Helvetica', 15, 'italic'), text="Welcome to the Obstruction game!", fg="purple", bd=15,
                        anchor='w')
        title.grid(row=0, column=1)
        title.configure(bg='lavender')

        self.set(BoardGUI)

        self.start = Button(self, text="Start", bg="light green", height=2, width=10, command=lambda: self.start_game())
        self.start.grid(row=1, column=0)
        self.desc = Button(self, text="Description", width=10, height=2, bg="orange", command=lambda: self.description())
        self.desc.grid(row=1, column=1)
        self.ButtonQuit = Button(self, background="#DA2C43", text="Quit", height=2, width=10, command=lambda: Frame.quit(self))
        self.ButtonQuit.grid(row=1, column=2)

    def set(self, game_frame):
        self.game = game_frame

    @staticmethod
    def description():
        messagebox.showinfo("Description", "Players take turns in marking squares on a grid. The first player unable to move loses. You are 'O' and the computer is 'X'.The players take turns in writing their symbol in an empty cell. Placing a symbol blocks all of the neighbouring cells from both players.")

    def start_game(self):
        self._controller.show_frame(self.game)


class GUI:
    def __init__(self, game):
        self._game = game
        self.tk = Tk()
        self.tk.geometry("600x500")
        self.tk.configure(bg ='lavender')
        self.tk.title("Obstruction game")

        all_frames = Frame(self.tk)
        all_frames.pack()

        self.frames = {}

        for frame in (StartGame, BoardGUI):
            fr = frame(all_frames, self, self._game)
            self.frames[frame] = fr
            fr.grid(row=0, column=0, sticky="nsew")
            fr.configure(bg='lavender')
        self.show_frame(StartGame)
        self.tk.mainloop()

    def show_frame(self, name):
        frame = name
        name = self.frames[name]
        if frame != StartGame:
            name.create_board()
            result = messagebox.askyesno("start", "Do you want to be the first player?")
            if result is not True:
                name.first_ai()
        name.tkraise()

    def quit_frame(self):
        self.show_frame(StartGame)


