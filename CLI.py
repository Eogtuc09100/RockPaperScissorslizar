from game_objects import Game, ComputerPlayer
import random

class CLI:
    def __init__(self):
        self.game = Game()

    def set_up(self):
        print(f"Game Begins\n------------")
        for i in range(2):
            player_type = "N/A"
            while player_type not in ["computer","player"]:
                player_type = input(f"Will player {i+1} be a player or a computer? ").lower()
            if player_type == "player":
                player_name = input(f"Player {i+1} name? ")
                self.game.add_human_player(player_name)
            else:
                self.game.add_computer_player()

        self.input_max_rounds()

    def input_max_rounds(self):
        mr = int(input("How many rounds? "))
        self.game.set_max_rounds(mr)

    def get_choices(self):
        for player in self.game.players:
            #print(isinstance(player, ComputerPlayer))
            if isinstance(player, ComputerPlayer):
                player.choose_object()
            else:
                choice = input(f"{player.name} choose your object. ")
                player.choose_object(choice)
        #print(player.current_object)

    def run_game(self):
        self.get_choices()
        self.game.find_winner()
        input(self.game.report_round())
        print(f"\n")
        input(self.game.report_score())
        print(f"\n")
        if not self.game.is_finished():
            self.game.next_round()

    def finished_game(self):
        print(self.game.report_winner())

        inp = "N/A"

        while inp not in ["1", "2"]:
            inp = input(f"\n1. Play again\n2. Main Menu\n")

        if inp == "1":
            self.game.reset()
            self.run_sequence()

        else:
            self.game.full_reset()

    def run_sequence(self):
        while not self.game.is_finished():
            self.run_game()
        self.finished_game()

    def menu(self):
        print(f"Welcome to the game!\n")
        print(f"1. New Game\n2. Exit")

        inp = ""
        while inp not in ["1", "2"]:
            inp = input()

        if inp == "1":
            self.set_up()
            self.run_sequence()

        else:
            quit()



if __name__ == "__main__":
    cli = CLI()
    cli.menu()