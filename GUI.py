from game_objects import Game, ComputerPlayer
import tkinter as Tk

class GUI(Tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('350x200')
        self.title('RPSLS')

        self.main_menu = MainMenu(self)
        self.main_menu.pack()


class MainMenu(Tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.title_label = Tk.Label(master, text="RPSLS", font=65)
        self.newgame_button = Tk.Button(master, text="New Game", command=self.newgame)
        self.exit_button = Tk.Button(master, text="Exit", command=quit)

        self.pack_widgets()

    def pack_widgets(self):
        self.title_label.pack()
        self.newgame_button.pack()
        self.exit_button.pack()

    def newgame(self):
        ...


if __name__ == '__main__':
    main_window = GUI()
    main_window.mainloop()