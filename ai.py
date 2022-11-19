from player import Player

class Ai(Player):
    def __init__(self) -> None:
        super().__init__()
        self.gesture_list = self.gesture_list

import random

def spur_list(list):
    randomized_choice = (random.choice(list))
    return randomized_choice

randomly_selected_pick = spur_list(Ai.gesture_list)
print(randomly_selected_pick)

