# Import game object and useful tkinter packagess
import tkinter as tk
from game_objects import Game, PlayerObject, HumanPlayer
from tkinter import ttk


class GameApp(tk.Tk):
    """ GameApp initialises a game and a Tk instance (window)
    The window includes a title and sets up frames with the different views on the game
    The show_frame method unpacks all the frames except for the one that needs to be shown """

    def __init__(self):
        super().__init__()
        self.game = create_game()
        title_string = ", ".join(obj.title() for obj in PlayerObject.allowable_objects) + " Game"

        # Set the window title
        self.title(title_string)
        # self.geometry("300x250")

        # Create a dictionary of frames. The key identifies the frame and the value is an instance of the
        # frame object
        self.frames = {
            "main_menu_frame": MainMenu(self),
            "setup_frame": Setup(self),
            "choose_object_frame": ChooseObject(self),
            "report_round_frame": ReportRound(self),
            "game_over_frame": GameOver(self)}

        # Show the GameOptionsGUI frame
        self.show_frame("main_menu_frame")

    # Function to show the desired game class, which is a subclass of tk.Frame
    def show_frame(self, current_frame: str):
        widgets = self.winfo_children()
        # Forget all the existing frames
        for w in widgets:
            if w.winfo_class() == "Frame":
                w.pack_forget()

        # Find and pack the current_frame
        frame_to_show = self.frames[current_frame]
        frame_to_show.pack(expand=True, fill=tk.BOTH)
        frame_to_show.setup()


class MainMenu(tk.Frame):

    # widgets created and then packed when frame is initialised
    def __init__(self, controller: GameApp):
        super().__init__()
        self.controller = controller
        self.title_label = tk.Label(self, text="RPSLS", font=65)
        self.newgame_button = tk.Button(self, text="New Game", command=self.next_frame)
        self.exit_button = tk.Button(self, text="Exit", command=quit)

        self.pack_widgets()

    # widgets gridded
    def pack_widgets(self):
        self.title_label.grid(row=0, column=0)
        self.newgame_button.grid(row=1, column=0)
        self.exit_button.grid(row=2, column=0)

    # empty setup as nothing needs to be done
    def setup(self):
        ...

    # starts the next frame
    def next_frame(self):
        self.controller.show_frame("setup_frame")


class Setup(tk.Frame):
    # combo-boxes, entries and labels created for setup
    def __init__(self, controller: GameApp):
        super().__init__()
        self.controller = controller
        self.player1_label = tk.Label(self, text="Player 1:")
        self.player1_type_label = tk.Label(self, text="Type:")

        self.player2_label = tk.Label(self, text="Player 2:")
        self.player2_type_label = tk.Label(self, text="Type:")

        self.player1_name_label = tk.Label(self, text="Name:")
        self.player1_name_entry = tk.Entry(self)

        self.player2_name_label = tk.Label(self, text="Name:")
        self.player2_name_entry = tk.Entry(self)

        # changes in state of combo-box detected to freeze computer name when needed
        self.player1_comboboxv = tk.StringVar()
        self.player1_type_combobox = ttk.Combobox(self, textvariable=self.player1_comboboxv,
                                                  values=["Computer", "Player"])
        self.player1_type_combobox.current(1)
        self.player1_comboboxv.trace('w', self.combobox_change)

        self.player2_comboboxv = tk.StringVar()
        self.player2_type_combobox = ttk.Combobox(self, textvariable=self.player2_comboboxv,
                                                  values=["Computer", "Player"])
        self.player2_type_combobox.current(1)
        self.player2_comboboxv.trace('w', self.combobox_change)

        self.max_rounds_label = tk.Label(self, text="Max Rounds:")
        self.max_rounds_entry = tk.Entry(self)

        self.confirm_button = tk.Button(self, text="Confirm", command=self.submit_setup)

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

    def setup(self):
        ...

    # protocol for when change in state in combo-box happens
    def combobox_change(self, x, y, z):
        if self.player1_type_combobox.get() == "Computer":
            self.player1_name_entry.delete(0, "end")
            self.player1_name_entry.configure(state="disabled")
        else:
            self.player1_name_entry.configure(state="normal")

        if self.player2_type_combobox.get() == "Computer":
            self.player2_name_entry.delete(0, "end")
            self.player2_name_entry.configure(state="disabled")
        else:
            self.player2_name_entry.configure(state="normal")

    # using the controller we pull inputs and create human/computer players whilst setting max rounds.
    def submit_setup(self):
        if self.player1_type_combobox.get() == "Computer":
            self.controller.game.add_computer_player()

        else:
            self.controller.game.add_human_player(self.player1_name_entry.get())

        if self.player2_type_combobox.get() == "Computer":
            self.controller.game.add_computer_player()

        else:
            self.controller.game.add_human_player(self.player2_name_entry.get())

        self.controller.game.set_max_rounds(int(self.max_rounds_entry.get()))
        self.controller.show_frame("choose_object_frame")


class ChooseObject(tk.Frame):

    # two comboboxes for choices of player 1 and player 2 are setup
    def __init__(self, controller: GameApp):
        super().__init__()
        self.controller = controller

        self.player1_name = tk.StringVar()
        self.player2_name = tk.StringVar()

        self.player1_name_label = tk.Label(self, textvariable=self.player1_name)
        self.choice1_combobox = ttk.Combobox(self, values=["rock", "paper", "scissors", "lizard", "spock"])
        self.choice1_combobox.current(1)
        self.player2_name_label = tk.Label(self, textvariable=self.player2_name)
        self.choice2_combobox = ttk.Combobox(self, values=["rock", "paper", "scissors", "lizard", "spock"])
        self.choice2_combobox.current(1)
        self.submit_choice_button = tk.Button(self, text="Submit", command=self.submit_choices)

        self.pack_choice_gui()

    def pack_choice_gui(self):
        self.player1_name_label.grid(row=0, column=0)
        self.choice1_combobox.grid(row=0, column=1)
        self.player2_name_label.grid(row=1, column=0)
        self.choice2_combobox.grid(row=1, column=1)
        self.submit_choice_button.grid(row=2, column=0, columnspan=2)

    # whether combobox is used depends on whether player1/2 is a computer
    def setup(self):
        # names of players set to string var for use in GUI
        self.player1_name.set(self.controller.game.players[0].name)
        self.player2_name.set(self.controller.game.players[1].name)

        if isinstance(self.controller.game.players[0], HumanPlayer):
            self.choice1_combobox.configure(state="enabled")
        else:
            self.choice1_combobox.configure(state="disabled")

        if isinstance(self.controller.game.players[1], HumanPlayer):
            self.choice2_combobox.configure(state="enabled")
        else:
            self.choice2_combobox.configure(state="disabled")

    # when submit is pressed current choices are submitted
    def submit_choices(self):
        self.choice1 = self.choice1_combobox.get()
        self.choice2 = self.choice2_combobox.get()

        player1 = self.controller.game.players[0]
        player2 = self.controller.game.players[1]

        if isinstance(player1, HumanPlayer):
            player1.choose_object(self.choice1)
        else:
            player1.choose_object()

        if isinstance(player2, HumanPlayer):
            player2.choose_object(self.choice2)
        else:
            player2.choose_object()

        self.controller.show_frame("report_round_frame")


class ReportRound(tk.Frame):
    #report round text is gridded
    def __init__(self, controller: GameApp):
        super().__init__()
        self.controller = controller

        self.round_result = tk.StringVar()
        self.report_score = tk.StringVar()

        self.report_round_label = tk.Label(self, textvariable=self.round_result)
        self.report_score_label = tk.Label(self, textvariable=self.report_score)
        self.next_round_button = tk.Button(self, text="Next Round", command=self.next_round)

        self.pack_widgets()

    def pack_widgets(self):
        self.report_round_label.grid(row=0, column=0, columnspan=3)
        self.report_score_label.grid(row=1, column=0, columnspan=3)
        self.next_round_button.grid(row=5, column=0, columnspan=3)

    def setup(self):
        self.controller.game.find_winner()
        self.round_result.set(self.controller.game.report_round())
        self.report_score.set(self.controller.game.report_score())

    # depending on whether the game is over you return to choose another object or the game ends.
    def next_round(self):
        if self.controller.game.is_finished():
            self.controller.show_frame("game_over_frame")
        else:
            self.controller.game.next_round()
            self.controller.show_frame("choose_object_frame")


class GameOver(tk.Frame):
    def __init__(self, controller: GameApp):
        super().__init__()
        self.controller = controller

        self.report_winner = tk.StringVar()

        self.report_winner_label = tk.Label(self, textvariable=self.report_winner)
        self.play_again_button = tk.Button(self, text="Play Again", command=self.play_again)
        self.main_menu_button = tk.Button(self, text="Main Menu", command=self.main_menu)

        self.pack_widgets()

    def pack_widgets(self):
        self.report_winner_label.grid(row=0, column=0)
        self.play_again_button.grid(row=1, column=0)
        self.main_menu_button.grid(row=1, column=1)

    def setup(self):
        self.report_winner.set(self.controller.game.report_winner())

    # you can play again or return to the main menu
    def play_again(self):
        self.controller.game.reset()
        self.controller.show_frame("choose_object_frame")

    def main_menu(self):
        self.controller.game.full_reset()
        self.controller.show_frame("main_menu_frame")


def create_game():
    game = Game()
    return game


if __name__ == "__main__":
    app = GameApp()
    app.mainloop()

