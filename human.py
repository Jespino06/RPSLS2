from player import Player

class Human(Player):
    def __init__(self, name):
        super().__init__(name)
        pass
        
    def choose_gesture(self):
        user_input_int = int(input('Please choose from the following options: 0. Rock, 1. Paper 2. Scissor, 3. Spock, 4. Lizard '))
        self.chosen_gesture = self.gesture_list[user_input_int]
        
        while True:
            self.player = self.chosen_gesture 
            if self.player_one == "Rock":
                self.player_one = [0]
                print('Player one, chose Rock!')
            elif self.player_one == "Paper":
                self.player_one = [1]
                print('Player one, chose Paper!')
            elif self.player_one == "Scissor":
                self.player_one = [2]
                print('Player one, chose Scissor!')
            elif self.player_one == "Spock":
                self.player_one = [3]
                print('Player one, chose Spock!')
            elif self.player_one == "Lizard":
                self.player_one = [4]
                print('Player one, chose Lizard!')
                return self.player_one

            while True:
                self.player = self.chosen_gesture
                if self.player_two == "Rock":
                    self.player_two = [0]
                    print('Player two, chose Rock!')
                elif self.player_two == "Paper":
                    self.player_two = [1]
                    print('Player two, chose Paper!')
                elif self.player_two == "Scissor":
                    self.player_two = [2]
                    print('Player two, chose Scissor!')
                elif self.player_two == "Spock":
                    self.player_two = [3]
                    print('Player two, chose Spock!')
                elif self.player_two == "Lizard":
                    self.player_two = [4]
                    print('Player two, chose Lizard!')
                    return self.player_two
        
        
        


         

        
                
                
                


            
    
    
   
    
    
        # self.gesture_option = self.gesture_option
        # self.chosen_gesture = self.gesture_list[user_input_int -1]