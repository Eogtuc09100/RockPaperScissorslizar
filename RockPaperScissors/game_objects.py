"""
Module contains the class objects that control the underlying logic for rock-paper scissors game.
...
Classes
-------
    PlayerObject
    Player
    HumanPlayer (subclass of Player)
    ComputerPlayer (subclass of Player
    Game

"""
import random

# constants
RPSLS_OBJECTS = ('rock', 'paper', 'scissors', 'lizard', 'spock')
RPSLS_WIN_DICT = {'rock': ['scissors', 'lizard'],
                  'scissors': ['paper', 'lizard'],
                  'paper': ['rock', 'spock'],
                  'lizard': ['paper', 'spock'],
                  'spock': ['rock', 'scissors'],
                  }
RPS_OBJECTS = ('rock', 'paper', 'scissors')
RPS_WIN_DICT = {'rock': ['scissors'],
                'scissors': ['paper'],
                'paper': ['rock'],
                }


# PlayerObject represents an object that a player could choose
class PlayerObject:
    """
    A class to represent a playable object
    ...
    Attributes
    ----------
    name: str
        name of the object
    allowable_objects: tuple (class attribute)
        list of allowable objects
    win_dict: dict
        keys are allowable objects, values is list of what keys will beat
    Methods
    -------
    random_objects (class method)
        returns a PlayerObject randomly chosen from the allowable objects
    set_object_rules (class method)
        sets the allowable objects and the win_dict for what the object can beat
    """

    # Set default objects for the class
    allowable_objects = RPSLS_OBJECTS
    win_dict = RPSLS_WIN_DICT

    def __init__(self, name):
        """
        Constructs the attributes for the PlayerObject

        Parameters
        ----------
            name: str
                name of object - must be in allowable objects
        """
        self.name = name
        if self.name not in self.allowable_objects:
            raise ValueError
        ...

    @classmethod
    def random_object(cls):
        """
        Returns a random object from amongst the allowable objects
        """
        # The allowable objects are in cls.allowable_objects
        return PlayerObject(random.choice(cls.allowable_objects))

    @classmethod
    def set_object_rules(cls, allowable_objects=None, win_dict=None):
        """
        Sets the allowable objects and the win_dict for the class
        """
        # Leave this for now!
        ...

    def __eq__(self, other):
        """
        Returns True if the name attribute of self and other are the same
        """

        return self.name == other.name

    def __gt__(self, other):
        """
        Checks if the current object (self) beats the passed object (other), by checking win_dict
        """
        return other.name in self.win_dict[self.name]

    def __repr__(self):
        """
        Representation of the object
        """
        return f'PlayerObject("{self.name}")'


# The Player Class represents a player
class Player:
    """
    A class to represent a player of the game

    Attributes
    __________
        name: str
            Player name
        score: int
            Player score
        current_object: PlayerObject or None
            What the player's current object is None for not selected
    """

    def __init__(self, name=None):
        """
        Constructs the necessary attributes for the Player class
        """
        self.name = name
        self.score = 0
        self.current_object = None

    def set_name(self, name):
        """ Sets name attribute to name """
        self.name = name

    def reset_object(self):
        """ Sets the current_object to None - not selected"""
        self.current_object = None

    def win_round(self):
        """ Increases score by one """
        self.score += 1

    def __repr__(self):
        """ Representation of the object """
        check_object_chosen = bool(self.current_object)
        return f'Player: {self.name}\nScore: {self.score}\nObject chosen: {check_object_chosen}'


# The HumanPlayer Class is a subclass of Player representing a human player
class HumanPlayer(Player):
    """ Subclass of Player representing a human player (PC) """

    def choose_object(self, choice):
        """ Chooses a PlayerObject for the player"""
        self.current_object = PlayerObject(choice)


# The ComputerPlayer Class is a subclass of Player representing a Computer player
class ComputerPlayer(Player):
    """ Subclass of Player representing a Computer player (NPC) """

    def __init__(self):
        """ Constructs super Player object with name "Computer """
        super().__init__("Computer")

    def choose_object(self):
        """ Computer chooses a random PlayerObject """
        self.current_object = PlayerObject.random_object()


# The Game class contains the instructions for running the game
class Game:
    """
    A class representing the Rock, Paper Scissors Game
    Attributes
    __________
        allowable_objects (opt)
            list of allowable objects
        win_dict (opt)
            dict showing what objects the object in the key beats
        current_round: int
            the current round
        max_rounds: int
            the maximum rounds that can be played
        round_result
            None (not played), draw or win
        round_winner
            the PlayerObject for the round winner (None if no winner)
    """

    def __init__(self, allowable_objects=None, win_dict=None):
        if allowable_objects is None:
            allowable_objects = RPSLS_OBJECTS
        if win_dict is None:
            win_dict = RPSLS_WIN_DICT

        self.players = []
        self.max_rounds = 3

    def add_human_player(self, name=None):
        """ Add a human player with their name and appends it to players"""
        self.players.append(HumanPlayer(name))

    def add_computer_player(self):
        """ Add a computer player (no name) """
        self.players.append(ComputerPlayer)

    def set_max_rounds(self, mr):
        """ Set the maximum number of rounds """
        self.max_rounds = mr

    def find_winner(self):
        """ Finds the winner of the current round """
        ...

    def next_round(self):
        """ Resets game objects ready for a new round """
        ...

    def is_finished(self):
        """ Checks if game is finished """
        ...

    def reset(self):
        """ Resets the whole game, setting current round to 0 and player scores to 0"""
        ...

    def report_round(self):
        """ returns a message reporting on what the players played and what the result of the round was """
        ...

    def report_score(self):
        """ Returns a string with the current scores """
        ...

    def report_winner(self):
        """ Returns a message with the overall winner """
        ...
