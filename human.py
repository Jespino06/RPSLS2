from player import Player

class Human(Player):
    def __init__(self, name):
        super().__init__(name)
        
    def choose_gesture(self):
        user_input_int = int(input('Please choose from the following options: 1. Rock, 2. Paper 3. Scissor, 4. Spock, 5. Lizard '))
        self.chosen_gesture = self.gesture_list[user_input_int-1]
    

    
    
        # self.gesture_option = self.gesture_option