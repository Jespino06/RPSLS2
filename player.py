class Player:
    def __init__(self, name):
        self.name = name
        self.gesture_list = ['Rock', 'Paper', 'Scissor', 'Spock', 'Lizard']
        self.score = 0
        self.chosen_gesture = ""
        pass

    
    def gesture_options(self):
        self.player_one = 0
        self.player_two = 0
        self.ai_one = 0
        self.ai_two = 0
        txt = "Player, you win!" or "Computer, you win!"
        s = txt.count('Player, you win' or 'Computer, you win!')

        
        while self.player_one or self.player_two == self.ai_one or self.ai_two == True:
            if self.player_one or self.player_two == self.ai_one or self.ai_two:
                print('Oh my you have a tie!!!')
            user_input = input('Play again? Y/N. ')
            if user_input == 'Y':
                continue
            elif user_input == 'N':
                print ('Game over')
            elif self.player_one or self.player_two == 'Rock':
                if self.ai_one or self.ai_two == 'Scissors':
                    print('Rock crushes Scissors. Player, you win!')
            elif self.player_one or self.player_two == 'Scissors':
                if self.ai_one or self.ai_two == 'Paper':
                    print('Scissors cuts Paper. Player, you win!')
            elif self.player_one or self.player_two == "Paper":
                if self.ai_one or self.ai_two == 'Rock':
                    print('Paper covers Rock. Player, you win!')
            elif self.player_one or self.player_two == 'Rock':
                if self.ai_one or self.ai_two == 'Lizard':
                    print('Rock crushes Lizard. Player, you win!!')
            elif self.player_one or self.player_two == 'Lizard':
                if self.ai_one or self.ai_two == 'Spock':
                    print('Lizard poisons Spock. Player, you win!')
            elif self.player_one or self.player_two == 'Spock':
                if self.ai_one or self.ai_two == 'Scissors':
                    print('Spock smashes Scissors. Player, you win!')
            elif self.player_one or self.player_two == 'Scissors':
                if self.ai_one or self.ai_two == 'Lizard':
                    print('Scissors decapitates Lizard. Player, you win!')
            elif self.player_one or self.player_two == 'Lizard':
                if self.ai_one or self.ai_two == 'Paper':
                    print('Lizard eats Paper. Player, you win')
            elif self.player_one or self.player_two == 'Paper':
                if self.ai_one or self.ai_two == 'Spock':
                    print('Paper disproves Spock. Player, you win!')
            elif self.player_one or self.player_two == 'Spock':
                if self.ai_one or self.ai_two == 'Rock':
                    print('Spock vaporizes Rock. Player, you win!')
            elif self.ai_one or self.ai_two == 'Rock':
                if self.player_one or self.player_two == 'Scissors':
                    print('Rock crushes Scissors. Computer, you win!')
            elif self.ai_one or self.ai_two == 'Scissors':
                if self.player_one or self.player_two == 'Paper':
                    print('Scissors cuts Paper. Computer, you win!')
            elif self.ai_one or self.ai_two == "Paper":
                if self.player_one or self.player_two == 'Rock':
                    print('Paper covers Rock. Computer, you win!')
            elif self.ai_one or self.ai_two == 'Rock':
                if self.player_one or self.player_two == 'Lizard':
                    print('Rock crushes Lizard. Computer, you win!!')
            elif self.ai_one or self.ai_two == 'Lizard':
                if self.player_one or self.player_two == 'Spock':
                    print('Lizard poisons Spock. Computer, you win!')
            elif self.ai_one or self.ai_two == 'Spock':
                if self.player_one or self.player_two == 'Scissors':
                    print('Spock smashes Scissors. Computer, you win!')
            elif self.ai_one or self.ai_two == 'Scissors':
                if self.player_one or self.player_two == 'Lizard':
                    print('Scissors decapitates Lizard. Computer, you win!')
            elif self.ai_one or self.ai_two == 'Lizard':
                if self.player_one or self.player_two == 'Paper':
                    print('Lizard eats Paper. Computer, you win')
            elif self.ai_one or self.ai_two == 'Paper':
                if self.player_one or self.player_two == 'Spock':
                    print('Paper disproves Spock. Computer, you win!')
            elif self.ai_one or self.ai_two == 'Spock':
                if self.player_one or self.player_two == 'Rock':
                    print('Spock vaporizes Rock. Computer, you win!')
            self.human1 +=1
            self.human2 +=1
            self.ai +=1 
            self.ai_two +=1
            print(s) 
            self.human1 +=1
            self.human2 +=1
            self.ai +=1 
            self.ai_two +=1
            print(s)    
   

    

   