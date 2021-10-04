from random import choice

class Lottery:
    def __init__(self):
        self.number = ("1", "2","3","4","5","a","b","c","d","e")
    
    def draw_number(self):
        winning_number = []
        for _x in range(1,5):
            winning_number.append(choice(self.number))
        return winning_number
        
draw = Lottery()
print(f'Winning number : {"".join(draw.draw_number())}')


