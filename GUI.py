from game_objects import Game, ComputerPlayer
import tkinter as Tk
from tkinter import ttk

class GUI(Tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('350x300')
        self.title('RPSLS')

        self.main_menu = MainMenu(self)
        self.main_menu.pack()


class MainMenu(Tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.title_label = Tk.Label(self, text="RPSLS", font=65)
        self.newgame_button = Tk.Button(self, text="New Game", command=self.newgame)
        self.exit_button = Tk.Button(self, text="Exit", command=quit)

        self.pack_widgets()

    def pack_widgets(self):
        self.title_label.grid(row=0, column=0)
        self.newgame_button.grid(row=1, column=0)
        self.exit_button.grid(row=2, column=0)

    def newgame(self):
        self.setup_game = SetupGame(self.master)
        self.setup_game.pack()
        self.pack_forget()

class SetupGame(Tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.player1_label = Tk.Label(self, text="Player 1:")
        self.player1_type_label = Tk.Label(self, text="Type:")
        self.player1_type_combobox = ttk.Combobox(self, values=["Computer","Player"])
        self.player1_type_combobox.current(1)
        self.player1_name_label = Tk.Label(self, text="Name:")
        self.player1_name_entry = Tk.Entry(self)

        self.player2_label = Tk.Label(self, text="Player 2:")
        self.player2_type_label = Tk.Label(self, text="Type:")
        self.player2_type_combobox = ttk.Combobox(self, values=["Computer","Player"])
        self.player2_type_combobox.current(1)
        self.player2_name_label = Tk.Label(self, text="Name:")
        self.player2_name_entry = Tk.Entry(self)

        self.max_rounds_label = Tk.Label(self, text="Max Rounds:")
        self.max_rounds_entry = Tk.Entry(self)

        self.confirm_button = Tk.Button(self, text="Confirm", command=self.load_game)

        self.pack_widgets()

    def pack_widgets(self):
        self.player1_label.grid(row=0, column=0)
        self.player1_type_label.grid(row=1, column=0)
        self.player1_type_combobox.grid(row=1, column=1)
        self.player1_name_label.grid(row=2, column=0)
        self.player1_name_entry.grid(row=2, column=1)

        self.player2_label.grid(row=3, column=0)
        self.player2_type_label.grid(row=4, column=0)
        self.player2_type_combobox.grid(row=4, column=1)
        self.player2_name_label.grid(row=5, column=0)
        self.player2_name_entry.grid(row=5, column=1)

        self.max_rounds_label.grid(row=6, column=0, pady=20)
        self.max_rounds_entry.grid(row=6, column=1, pady=20)

        self.confirm_button.grid(row=7, column=0, columnspan=2)

    def load_game(self):
        self.game_screen = GameScreen(self.master)
        self.game_screen.pack()
        self.pack_forget()

class GameScreen(Tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.submit_choice_button = Tk.Button(self, text="Submit", command=self.submit_choice)

        self.next_round_button = Tk.Button(self, text="Next Round", command=self.next_round)

        self.pack_round()

    def pack_round(self):
        self.submit_choice_button.grid(row=5, column=0, columnspan=3)

    def unpack_round(self):
        self.submit_choice_button.grid_remove()

    def pack_report_round(self):
        self.next_round_button.grid(row =5, column=0, columnspan=3)

    def unpack_report_round(self):
        self.next_round_button.grid_remove()

    def submit_choice(self):
        self.unpack_round()
        
        self.pack_report_round()

    def next_round(self):
        self.unpack_report_round()

        self.pack_round()

    def game_sequence(self):
        ...


if __name__ == '__main__':
    main_window = GUI()
    main_window.mainloop()
