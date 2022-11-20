from player import Player

class Human(Player):
    def __init__(self, name, gesture_list):
        super().__init__(name, gesture_list)
        self.name = name
        self.gesture_list = gesture_list

    

    
    
    
        # self.gesture_option = self.gesture_option