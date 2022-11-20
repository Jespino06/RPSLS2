from human import Human
from ai import Ai


class Game:
    def __init__(self):
        self.human1 = Human('player1', '')
        self.human2 = Human('player2', '')
        self.ai = Ai('computer1', "")
        self.ai_two = Ai('computer2',"")
        pass

    def intro_message(self):
        self.welcome = 'Welcome to Rock, Scissor, Spock, and Lizard. Let the game begin!'
        print(self.welcome)
        self.rules = 'Here are the rules of the game: In a round of three games you would select a number according to which item you would like to be. Out of those three games you would be the winner. Good luck!!'
        print(self.rules)

    print()   
    print()


    def display_gesture_options(self):
        print('Rock crushes Scissors')
        print('Scissors cuts Paper')
        print('Paper covers Rock')
        print('Rock crushes Lizard')
        print('Lizard poisons Spock')
        print('Spock smashes Scissors')
        print('Scissors decapitates Lizard')
        print('Lizard eats Paper')
        print('Paper disproves Spock')
        print('Spock vaporizes Rock')
    
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
        self.human1 = 0
        self.human2 = 0
        self.ai = 0
        self.ai_two
        txt = "Player, you win!"
        s = txt.count('Player, you win')

        x = int(input('Please choose from the following options: 1. Rock, 2. Paper 3. Scissor, 4. Spock, 5. Lizard '))
        if self.human1 and self.human2 == 'Rock':
            if self.ai == 'Scissors':
                print('Rock crushes Scissors. Player, you win!')
        elif self.human1 and self.human2 == 'Scissors':
            if self.ai == 'Paper':
                print('Scissors cuts Paper. Player, you win!')
        elif self.human1 and self.human2 == "Paper":
            if self.ai == 'Rock':
                print('Paper covers Rock. Player, you win!')
        elif self.human1 and self.human2 == 'Rock':
            if self.ai == 'Lizard':
                print('Rock crushes Lizard. Player, you win!!')
        elif self.human1 and self.human2 == 'Lizard':
            if self.ai == 'Spock':
                print('Lizard poisons Spock. Player, you win!')
        elif self.human1 and self.human2 == 'Spock':
            if self.ai == 'Scissors':
                print('Spock smashes Scissors. Player, you win!')
        elif self.human1 and self.human2 == 'Scissors':
            if self.ai == 'Lizard':
                print('Scissors decapitates Lizard. Player, you win!')
        elif self.human1 and self.human2 == 'Lizard':
            if self.ai == 'Paper':
                print('Lizard eats Paper. Player, you win')
        elif self.human1 and self.human2 == 'Paper':
            if self.ai == 'Spock':
                print('Paper disproves Spock. Player, you win!')
        elif self.human1 and self.human2 == 'Spock':
            if self.ai == 'Rock':
                print('Spock vaporizes Rock. Player, you win!')
        elif self.human1 and self.human2 == self.ai:
            print('Oh my you have a tie!!!')
            self.human1 +=1
            self.human2 +=1
            self.ai +=1 
            self.ai_two +=1
            print(s)    
    
    def run_game(self):
        self.intro_message()
        self.display_gesture_options()
        self.num_of_players()
        self.gesture_options()

    
    
    
    

    




    
    
    # def display_gesture_options(self):
    #     print(Player.options_list[0])
    #     print(Player.options_list[1])
    #     print(Player.options_list[2])
    #     print(Player.options_list[3])
    #     print(Player.options_list[4])
    #     print(Player.options_list[5])
    #     print(Player.options_list[6])
    #     print(Player.options_list[7])
    #     print(Player.options_list[8])
    #     print(Player.options_list[9])