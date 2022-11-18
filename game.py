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

    def num_of_players(self):
        while True:
            try:
                num = int(input("How many will be playing? Enter 1, 2, or 3. "))
            except ValueError:
                print("There was an error, please enter a single digit number. ")
                continue
            if num <4 and num > 0:
                print(num)
                break
            else:
                print("There was an error, please enter a single digit number. ")

    def display_gesture_options(self):
        num = int(input('Please choose from the following options: 1. Rock, 2. Scissor, 3. Spock, 4. Lizard'))
        if num == 1:
            print('Rock')
        elif num == 2:
            print('Scissor')
        elif num == 3:
            print('Spock')
        elif num == 4:
            print('Lizard')
    
    def display_winner(self):
        

