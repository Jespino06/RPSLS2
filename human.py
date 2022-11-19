from player import Player

class Human(Player):
    def __init__(self):
        super().__init__()
        self.gesture_list = [Player.gesture_list]
        self.gesture_option = self.gesture_option

    def gesture_options(self):
        x = int(input('Please choose from the following options: 1. Rock, 2. Paper 3. Scissor, 4. Spock, 5. Lizard'))
        human1 = x
        human2 = x
        if human1 and human2 == 1:
            print('Rock')
        elif human1 and human2 == 2:
            print('Paper')
        elif human1 and human2 == 3:
            print('Scissor')
        elif human1 and human2 == 4:
            print('Spock')
        elif human1 and human2 == 5:
            print('Lizard')