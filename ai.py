from player import Player
import random

class Ai(Player):
    def __init__(self, name):
        super().__init__(name)
        self.picked_gesture = 'None'
        pass


    def choose_gesture(self):
        while True:
            self.picked_gesture = random.choice(self.gesture_list)
            break
        print(f'{self.name} has a chosen {self.picked_gesture}')

    
            
    
