class Player:
    def __init__(self, name):
        self.name = name
        self.gesture_list = ['Rock', 'Paper', 'Scissor', 'Spock', 'Lizard']
        self.score = 0
        self.picked_gesture= "None"
        pass
    
    def result(self, run):
        self.score = 0
        for x in range (5):
            if self.picked_gesture == self.gesture_list[x]:
                self.score = 1
            if self.score == 0:
                run = False
                return run
            if self.score == 1:
                self.picked_gesture = self.score
                run = True
                return run

    