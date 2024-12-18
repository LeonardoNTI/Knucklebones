import random

class Dice:
    @staticmethod
    def roll():
        """Kasta en tärning."""
        return random.randint(1, 6)