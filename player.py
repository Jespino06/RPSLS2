class Player:
    def __init__(self, name):
        self.name = name
        self.gesture_list = ['Rock', 'Paper', 'Scissor', 'Spock', 'Lizard']
        self.score = 0
        self.picked_gesture = "None"
        pass
    
    def result(self, run):
        s = 0
        for x in range (5):
            if self.picked_gesture == self.gesture_list[x]:
                s = 1
            if s == 0:
                run = False
                return run
            if s == 1:
                self.picked_gesture = self.score
                run = True
                return run

    