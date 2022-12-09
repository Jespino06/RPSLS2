from player import Player
import random

class Ai(Player):
    def __init__(self, name):
        super().__init__(name)
        pass


    def computer_gesture(self):

        while True:
            self.ai_gesture = (random.choice(self.gesture_list))
            if self.ai_gesture == "Rock":
                self.ai_gesture = [0]
                print('Computer, chose Rock!')
            elif self.ai_gesture == "Paper":
                self.ai_gesture = [1]
                print('Computer, chose Paper!')
            elif self.ai_gesture == "Scissor":
                self.ai_gesture = [2]
                print('Computer, chose Scissor!')
            elif self.ai_gesture == "Spock":
                self.ai_gesture = [3]
                print('Computer, chose Spock!')
            elif self.ai_gesture == "Lizard":
                self.ai_gesture = [4]
                print('Computer, chose Lizard!')
    
    