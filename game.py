from human import Human
from ai import Ai


class Game:
    def __init__(self):
        self.player = self.player_one = Human('player one')
        self.player = self.player_two = Human('player one')
        self.ai = self.ai_one = Ai('computer one)')
        self.ai = self.ai_two = Ai('computer two')
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
                user_input = int(input("How many will be playing? Enter 1, 2, or 3. "))
            except ValueError:
                print("There was an error, please enter a single digit number. ")
                continue
            if user_input <4 and user_input > 0:
                print(user_input)
                break
            else:
                print("There was an error, please enter a single digit number. ")
        
        if user_input == "1":

    
    
    print()
    print()

    
        
    
    def game_wins(self):
        self.player_one = 0
        self.player_two = 0
        self.ai_one = 0
        self.ai_two = 0
        txt = "Player, you win!" or "Computer, you win!"
        s = txt.count('Player, you win' or 'Computer, you win!')
        
    def run_game(self):
        self.intro_message()
        self.display_gesture_options()
        self.num_of_players()
        self.choose_gesture()
        


    def choosen_gesture(self):
        if self.player == self.ai_gesture:
            print('Oh my you have a tie!!!')
        elif self.player_one == 'Rock':
            if self.ai == 'Scissors':
                print('Rock crushes Scissors. Player one, you win!')
        elif self.player_one == 'Scissors':
            if self.ai == 'Paper':
                print('Scissors cuts Paper. Player one, you win!')
        elif self.player_one  == "Paper":
            if self.ai == 'Rock':
                print('Paper covers Rock. Player one, you win!')
        elif self.player_one  == 'Rock':
            if self.ai == 'Lizard':
                print('Rock crushes Lizard. Player one, you win!!')
        elif self.player_one  == 'Lizard':
            if self.ai == 'Spock':
                print('Lizard poisons Spock. Player one, you win!')
        elif self.player_one == 'Spock':
            if self.ai == 'Scissors':
                print('Spock smashes Scissors. Player one, you win!')
        elif self.player_one == 'Scissors':
            if self.ai == 'Lizard':
                print('Scissors decapitates Lizard. Player one, you win!')
        elif self.player_one == 'Lizard':
            if self.ai == 'Paper':
                print('Lizard eats Paper. Player one, you win')
        elif self.player_one == 'Paper':
            if self.ai== 'Spock':
                print('Paper disproves Spock. Player one, you win!')
        elif self.player_one == 'Spock':
            if self.ai == 'Rock':
                print('Spock vaporizes Rock. Player one, you win!')
        elif self.player_two== self.ai:
            print('Oh my you have a tie!!!')
        elif self.player_two == 'Rock':
            if self.ai == 'Scissors':
                print('Rock crushes Scissors. Player two, you win!')
        elif self.player_two == 'Scissors':
            if self.ai == 'Paper':
                print('Scissors cuts Paper. Player two, you win!')
        elif self.player_two  == "Paper":
            if self.ai == 'Rock':
                print('Paper covers Rock. Player two, you win!')
        elif self.player_two  == 'Rock':
            if self.ai == 'Lizard':
                print('Rock crushes Lizard. Player two, you win!!')
        elif self.player_two  == 'Lizard':
            if self.ai == 'Spock':
                print('Lizard poisons Spock. Player two, you win!')
        elif self.player_two == 'Spock':
            if self.ai == 'Scissors':
                print('Spock smashes Scissors. Player two, you win!')
        elif self.player_two == 'Scissors':
            if self.ai == 'Lizard':
                print('Scissors decapitates Lizard. Player two, you win!')
        elif self.player_two == 'Lizard':
            if self.ai == 'Paper':
                print('Lizard eats Paper. Player two, you win')
        elif self.player_two == 'Paper':
            if self.ai== 'Spock':
                print('Paper disproves Spock. Player two, you win!')
        elif self.player_two == 'Spock':
            if self.ai == 'Rock':
                print('Spock vaporizes Rock. Player two, you win!')
        while self.player_one or self.player_two == self.ai:
            user_input = input('Play again? Y/N. ')
            if user_input == 'Y':
                continue
            elif user_input == 'N':
                print ('Game over')
            self.player_one +=1
            self.player_two +=1
            self.ai_one +=1 
            self.ai_two +=1
            print(s)
   

    

   
        
        # if self.player_one or self.player_two == self.ai_one or self.ai_two:
        #     print('Oh my you have a tie!!!')
        # elif self.player_one or self.player_two == 'Rock':
        #     if self.ai_one or self.ai_two == 'Scissors':
        #         print('Rock crushes Scissors. Player, you win!')
        # elif self.player_one or self.player_two == 'Scissors':
        #     if self.ai_one or self.ai_two == 'Paper':
        #         print('Scissors cuts Paper. Player, you win!')
        # elif self.player_one or self.player_two == "Paper":
        #     if self.ai_one or self.ai_two == 'Rock':
        #         print('Paper covers Rock. Player, you win!')
        # elif self.player_one or self.player_two == 'Rock':
        #     if self.ai_one or self.ai_two == 'Lizard':
        #         print('Rock crushes Lizard. Player, you win!!')
        # elif self.player_one or self.player_two == 'Lizard':
        #     if self.ai_one or self.ai_two == 'Spock':
        #         print('Lizard poisons Spock. Player, you win!')
        # elif self.player_one or self.player_two == 'Spock':
        #     if self.ai_one or self.ai_two == 'Scissors':
        #         print('Spock smashes Scissors. Player, you win!')
        # elif self.player_one or self.player_two == 'Scissors':
        #     if self.ai_one or self.ai_two == 'Lizard':
        #         print('Scissors decapitates Lizard. Player, you win!')
        # elif self.player_one or self.player_two == 'Lizard':
        #     if self.ai_one or self.ai_two == 'Paper':
        #         print('Lizard eats Paper. Player, you win')
        # elif self.player_one or self.player_two == 'Paper':
        #     if self.ai_one or self.ai_two == 'Spock':
        #         print('Paper disproves Spock. Player, you win!')
        # elif self.player_one or self.player_two == 'Spock':
        #     if self.ai_one or self.ai_two == 'Rock':
        #         print('Spock vaporizes Rock. Player, you win!')
        # elif self.ai_one or self.ai_two == 'Rock':
        #     if self.player_one or self.player_two == 'Scissors':
        #         print('Rock crushes Scissors. Computer, you win!')
        # elif self.ai_one or self.ai_two == 'Scissors':
        #     if self.player_one or self.player_two == 'Paper':
        #         print('Scissors cuts Paper. Computer, you win!')
        # elif self.ai_one or self.ai_two == "Paper":
        #     if self.player_one or self.player_two == 'Rock':
        #         print('Paper covers Rock. Computer, you win!')
        # elif self.ai_one or self.ai_two == 'Rock':
        #     if self.player_one or self.player_two == 'Lizard':
        #         print('Rock crushes Lizard. Computer, you win!!')
        # elif self.ai_one or self.ai_two == 'Lizard':
        #     if self.player_one or self.player_two == 'Spock':
        #         print('Lizard poisons Spock. Computer, you win!')
        # elif self.ai_one or self.ai_two == 'Spock':
        #     if self.player_one or self.player_two == 'Scissors':
        #         print('Spock smashes Scissors. Computer, you win!')
        # elif self.ai_one or self.ai_two == 'Scissors':
        #     if self.player_one or self.player_two == 'Lizard':
        #         print('Scissors decapitates Lizard. Computer, you win!')
        # elif self.ai_one or self.ai_two == 'Lizard':
        #     if self.player_one or self.player_two == 'Paper':
        #         print('Lizard eats Paper. Computer, you win')
        # elif self.ai_one or self.ai_two == 'Paper':
        #     if self.player_one or self.player_two == 'Spock':
        #         print('Paper disproves Spock. Computer, you win!')
        # elif self.ai_one or self.ai_two == 'Spock':
        #     if self.player_one or self.player_two == 'Rock':
        #         print('Spock vaporizes Rock. Computer, you win!')
        
        # while self.player_one or self.player_two == self.ai_one or self.ai_two == True:
        #     user_input = input('Play again? Y/N. ')
        #     if user_input == 'Y':
        #         continue
        #     elif user_input == 'N':
        #         print ('Game over')
        #     self.player_one +=1
        #     self.player_two +=1
        #     self.ai_one +=1 
        #     self.ai_two +=1
        #     print(s) 
                





    # def chosen_gesture(self):
    #     self.player_one = int(input('Please choose from the following options: 1. Rock, 2. Paper 3. Scissor, 4. Spock, 5. Lizard '))
    #     self.player_two = int(input('Please choose from the following options: 1. Rock, 2. Paper 3. Scissor, 4. Spock, 5. Lizard '))

    #     if self.player_one == "Rock":
    #         self.player_one = 1
    #         print('Player one, chose Rock!')
    #     elif self.player_two == "Rock":
    #         self.player_two == 1
    #         print("Player two, chose Rock!")
    #     elif self.player_one == "Paper":
    #         self.player_one = 2
    #         print('Player one, chose Paper!')
    #     elif self.player_two == "Paper":
    #         self.player_two = 2
    #         print('Player two, chose Paper!')
    #     elif self.player_one == "Scissor":
    #         self.player_one = 3
    #         print('Player one, chose Scissor!')
    #     elif self.player_two == "Scissor":
    #         self.player_two = 3
    #         print('Player two, chose Scissor!')
    #     elif self.player_one == "Spock":
    #         self.player_one = 4
    #         print('Player one, chose Spock!')
    #     elif self.player_two == "Spock":
    #         self.player_two = 4
    #         print('Player two, chose Spock!')
    #     elif self.player_one == "Lizard":
    #         self.player_one = 5
    #         print('Player one, chose Lizard!')
    #     elif self.player_two == "Lizard":
    #         self.player_two = 5
    #         print('Player two, chose Lizard')
    #     print(self.player_one)
    #     print(self.player_two)


        

    
        


    
    # def gesture_options(self):
    #     self.player_one = 0
    #     self.player_two = 0
    #     self.ai_one = 0
    #     self.ai_two = 0
    #     txt = "Player, you win!" or "Computer, you win!"
    #     s = txt.count('Player, you win' or 'Computer, you win!')

    #     x = int(input('Please choose from the following options: 1. Rock, 2. Paper 3. Scissor, 4. Spock, 5. Lizard '))
    #     if self.player_one or self.player_two == self.ai_one or self.ai_two:
    #         print('Oh my you have a tie!!!')
    #     elif self.player_one or self.player_two == 'Rock':
    #         if self.ai_one or self.ai_two == 'Scissors':
    #             print('Rock crushes Scissors. Player, you win!')
    #     elif self.player_one or self.player_two == 'Scissors':
    #         if self.ai_one or self.ai_two == 'Paper':
    #             print('Scissors cuts Paper. Player, you win!')
    #     elif self.player_one or self.player_two == "Paper":
    #         if self.ai_one or self.ai_two == 'Rock':
    #             print('Paper covers Rock. Player, you win!')
    #     elif self.player_one or self.player_two == 'Rock':
    #         if self.ai_one or self.ai_two == 'Lizard':
    #             print('Rock crushes Lizard. Player, you win!!')
    #     elif self.player_one or self.player_two == 'Lizard':
    #         if self.ai_one or self.ai_two == 'Spock':
    #             print('Lizard poisons Spock. Player, you win!')
    #     elif self.player_one or self.player_two == 'Spock':
    #         if self.ai_one or self.ai_two == 'Scissors':
    #             print('Spock smashes Scissors. Player, you win!')
    #     elif self.player_one or self.player_two == 'Scissors':
    #         if self.ai_one or self.ai_two == 'Lizard':
    #             print('Scissors decapitates Lizard. Player, you win!')
    #     elif self.player_one or self.player_two == 'Lizard':
    #         if self.ai_one or self.ai_two == 'Paper':
    #             print('Lizard eats Paper. Player, you win')
    #     elif self.player_one or self.player_two == 'Paper':
    #         if self.ai_one or self.ai_two == 'Spock':
    #             print('Paper disproves Spock. Player, you win!')
    #     elif self.player_one or self.player_two == 'Spock':
    #         if self.ai_one or self.ai_two == 'Rock':
    #             print('Spock vaporizes Rock. Player, you win!')
    #     elif self.ai_one or self.ai_two == 'Rock':
    #         if self.player_one or self.player_two == 'Scissors':
    #             print('Rock crushes Scissors. Computer, you win!')
    #     elif self.ai_one or self.ai_two == 'Scissors':
    #         if self.player_one or self.player_two == 'Paper':
    #             print('Scissors cuts Paper. Computer, you win!')
    #     elif self.ai_one or self.ai_two == "Paper":
    #         if self.player_one or self.player_two == 'Rock':
    #             print('Paper covers Rock. Computer, you win!')
    #     elif self.ai_one or self.ai_two == 'Rock':
    #         if self.player_one or self.player_two == 'Lizard':
    #             print('Rock crushes Lizard. Computer, you win!!')
    #     elif self.ai_one or self.ai_two == 'Lizard':
    #         if self.player_one or self.player_two == 'Spock':
    #             print('Lizard poisons Spock. Computer, you win!')
    #     elif self.ai_one or self.ai_two == 'Spock':
    #         if self.player_one or self.player_two == 'Scissors':
    #             print('Spock smashes Scissors. Computer, you win!')
    #     elif self.ai_one or self.ai_two == 'Scissors':
    #         if self.player_one or self.player_two == 'Lizard':
    #             print('Scissors decapitates Lizard. Computer, you win!')
    #     elif self.ai_one or self.ai_two == 'Lizard':
    #         if self.player_one or self.player_two == 'Paper':
    #             print('Lizard eats Paper. Computer, you win')
    #     elif self.ai_one or self.ai_two == 'Paper':
    #         if self.player_one or self.player_two == 'Spock':
    #             print('Paper disproves Spock. Computer, you win!')
    #     elif self.ai_one or self.ai_two == 'Spock':
    #         if self.player_one or self.player_two == 'Rock':
    #             print('Spock vaporizes Rock. Computer, you win!')
    #         self.human1 +=1
    #         self.human2 +=1
    #         self.ai +=1 
    #         self.ai_two +=1
    #         print(s) 
    #         self.human1 +=1
    #         self.human2 +=1
    #         self.ai +=1 
    #         self.ai_two +=1
    #         print(s)    
    
        # self.gesture_options()

    
    
    # def toss_phase(self):
    #     import random

    #     self.ai = random.choice(Ai.gesture_list)


        

    

    




    
    
  