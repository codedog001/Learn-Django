import random

# Print random numbers like playing with 2 dice.

class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second # This way always a tuple is returned.


dice1 = Dice()
numbers = dice1.roll()
print(numbers)

