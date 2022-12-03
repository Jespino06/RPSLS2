from player import Player

class Human(Player):
    def __init__(self, name):
        super().__init__(name)
        pass
        
    def choose_gesture(self):
        user_input_int = int(input('Please choose from the following options: 1. Rock, 2. Paper 3. Scissor, 4. Spock, 5. Lizard '))
        self.chosen_gesture = self.gesture_list[user_input_int-1]
        self.player= ''
        
        
        while self.player == self.chosen_gesture:
            if self.player == [1]:
                print(self.player_one or self.player_two, 'chose Rock!')
            elif self.player == [2]:
                print(self.player_one or self.player_two, 'chose Paper!')
            elif self.player == [3]:
                print(self.player_one or self.player_two, 'chose Scissor!')
            elif self.player == [4]:
                print(self.player_one or self.player_two, 'chose Spock!')
            elif self.player == [5]:
                print(self.player_one or self.player_two, 'chose Lizard!')

        
                
                
                


            
    
    
   
    
    
        # self.gesture_option = self.gesture_option
        # self.chosen_gesture = self.gesture_list[user_input_int -1]