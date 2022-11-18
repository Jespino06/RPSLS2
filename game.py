from human import Human
from ai import Ai

class Game:
    def __init__(self):
        self.human = Human('Player_one')
        self.ai = Ai('Computer_one')
        pass

    def intro_message(self):
        self.welcome = 'Welcome to Rock, Scissor, Spock, and Lizard!'
        self.rules = 'Here are the rules of the game: In a round of three games you would select a number according to which item you would like to be. Out of those three games you would be the winner according to the number of rounds you won. Choose wisely, the game can be quite vicious, particularly with the opponent chosen! Good luck!!'
        pass

    
