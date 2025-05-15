import random
""" Description: Class object simulating an n sided die and rolling it
Author: Aaryaman jaising
Date 01/23/2025
"""
class Die:

    def __init__(self, num_sides):
        """Construct a new die with the given number of sides."""
        self.sides = num_sides
        self.value = 1 # default starting value

    def get_value(self):
        """Return value on die"""
        return self.value

    def roll(self):
        """ Roll the die"""
        self.value = random.randrange(1,self.sides+1)

    def __str__(self):
        return f"{self.sides}-sided die, current value: {self.value}"

def main():

    # TODO: create 8-sided dice (two die)
    die1 = Die(8)
    die2 = Die(8)


    # TODO: roll both until we get the same value
    die1.roll()
    die2.roll()
    while(die1.get_value() != die2.get_value()):
        die1.roll()
        die2.roll()
        print(die1)
        print(die2)
    print("Dice have now rolled the same value")
    print(die1)
    print(die2)
    
main()