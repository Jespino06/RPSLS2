from player import Player
import random

class Ai(Player):
    def __init__(self, name):
        super().__init__(name)
        pass


    def choose_gesture(self):
        self.chosen_gesture = int(random.choice(self.gesture_list))

        while self.ai == int(random.choice(self.gesture_list)-1):
            if self.chosen_gesture == [1]:
                print('Computer, chose Rock!')
            elif self.chosen_gesture == [2]:
                print('Computer, chose Paper!')
            elif self.chosen_gesture == [3]:
                print('Computer, chose Scissor!')
            elif self.chosen_gesture == [4]:
                print('Computer, chose Spock!')
            elif self.chosen_gesture == [5]:
                print('Computer, chose Lizard!')
               
                
                
                
                
        
    # def winning_gesture(self):
    #     if self.ai and self.player == :
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
        
     
   
