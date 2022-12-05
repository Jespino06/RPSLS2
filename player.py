class Player:
    def __init__(self, name):
        self.name = name
        self.gesture_list = ['Rock', 'Paper', 'Scissor', 'Spock', 'Lizard']
        self.score = 0
        self.chosen_gesture = ""
        pass
    

    def assign_player(self):

    
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
   

    

   