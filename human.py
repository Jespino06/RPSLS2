from player import Player

class Human(Player):
    def __init__(self, name):
        super().__init__(name)
        pass
        
    def choose_gesture(self):
        user_input_int = int(input('Please choose from the following options: 0. Rock, 1. Paper 2. Scissor, 3. Spock, 4. Lizard '))
        self.picked_gesture = self.gesture_list[user_input_int]
        print(f'{self.name} has chosen {self.picked_gesture}')


        
       
        
        
        


         

        
                
                
                


            
    
    
   
    
    