from game_objects import Game, PlayerObject, ComputerPlayer
import random

class CLI:
    def __init__(self):
        self.game = Game()

    def set_up(self):
        print(f"Game Begins\n------------")
        for i in range(2):
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
            if isinstance(player, ComputerPlayer):
                player.choose_object()
            else:
                choice = input(f"{player.name} choose your object. ")
                player.choose_object(choice)
            print(player.current_object)

    def run_game(self):
        self.get_choices()
        self.game.find_winner()
        print(self.game.report_round())
        print(self.game.report_score())
        if self.game.is_finished():
            print(self.game.report_winner())
        else:
            self.game.next_round()

    def run_sequence(self):
        self.set_up()
        while not self.game.is_finished():
            self.run_game()
        self.game.report_winner()

if __name__ == "__main__":
    cli = CLI()
    cli.run_sequence()