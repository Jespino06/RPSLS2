from human import Human
from ai import Ai
from player import Player

class Game:
    def __init__(self):
        self.human = Human('human1')
        self.human = Human('human2')
        self.ai = Ai('ai_1')
        self.ai = Ai('ai_2')
        pass

    def intro_message(self):
        self.welcome = 'Welcome to Rock, Scissor, Spock, and Lizard. Let the game begin!'
        print(self.welcome)
        self.rules = 'Here are the rules of the game: In a round of three games you would select a number according to which item you would like to be. Out of those three games you would be the winner. Good luck!!'
        print(self.rules)
       
    def display_gesture_options(self):
        print(Player.options_list[0])
        print(Player.options_list[1])
        print(Player.options_list[2])
        print(Player.options_list[3])
        print(Player.options_list[4])
        print(Player.options_list[5])
        print(Player.options_list[6])
        print(Player.options_list[7])
        print(Player.options_list[8])
        print(Player.options_list[9])
    
    print()
    
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

    print()

    def gesture_options(self):
        self.human = 0
        self.ai = 0
        
        x = int(input('Please choose from the following options: 1. Rock, 2. Paper 3. Scissor, 4. Spock, 5. Lizard'))
        if self.human == 'Rock':
            if self.ai == 'Scissors':
                print('Rock crushes Scissors. Thats a rough loss!')
        elif self.human == 'Scissors':
            if self.ai == 'Paper':
                print('Scissors cuts Paper. You got snipped!')
        elif self.human == "Paper":
            if self.ai == 'Rock':
                print('Paper covers Rock. You loss with no paper cuts!')
        elif self.human == 'Rock':
            if self.ai == 'Lizard':
                print('Rock crushes Lizard. Ouch that was a brutal loss!')
        elif self.human == 'Lizard':
            if self.ai == 'Spock':
                print('Lizard poisons Spock. What a harsh way to loose!')
        elif self.human == 'Spock':
            if self.ai == 'Scissors':
                print('Spock smashes Scissors. That was a smashing loss!')
        elif self.human == 'Scissors':
            if self.ai == 'Lizard':
                print('Scissors decapitates Lizard. Messy loss!')
        elif self.human == 'Lizard':
            if self.ai == 'Paper':
                print('Lizard eats Paper. Not a tasty loss!')
        elif self.human == 'Paper':
            if self.ai == 'Spock':
                print('Paper disproves Spock. You lose!')
        elif self.human == 'Spock':
            if self.ai == 'Rock':
                print('Spock vaporizes Rock. You got pulverized!')
        elif self.human == self.ai:
            print('Oh my you have a tie!!!')
            self.human +=1
            self.ai +=1     
    
    def run_game(self):
        self.intro_message()
        self.display_gesture_options()
        self.num_of_players()
        self.gesture_options()

    
    
    
    

    




    
    
    