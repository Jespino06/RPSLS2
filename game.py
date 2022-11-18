from human import Human
from ai import Ai

class Game:
    def __init__(self):
        self.human = Human('Player_one')
        self.ai = Ai('Computer_one')
        pass

    