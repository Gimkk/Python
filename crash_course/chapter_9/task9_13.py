from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides
    
    def roll_die(self):
        return randint(1,self.sides)

die_6_sides = Die()
die_10_sides = Die(10)
die_20_sides = Die(20)

for _x in range (1, 11):
    print(f"6 sided die rolled: {die_6_sides.roll_die()}")
    print(f"10 sided die rolled: {die_10_sides.roll_die()}")
    print(f"20 sided die rolled: {die_20_sides.roll_die()}\n")