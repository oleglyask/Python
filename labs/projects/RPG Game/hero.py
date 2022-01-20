import requests
import random
from sqlalchemy import Integer


class Hero:

    def __init__(self, name_length, max_strength) -> None:
        self.name = self.get_name(name_length)
        self.strength = max_strength
        self.max_strenth = max_strength

    def __str__(self) -> str:
        return f"name: {self.name}\nstrength: {self.strength}\nmax strength: {self.max_strenth}\n"

    def battle(self, other):
        win_chances = int(self.strength / (self.strength + other.strength) * 100)
        if random.randint(1, 100) > win_chances:
            pass
            # self lost
        else:
            pass
            # self won


        

            

    @staticmethod
    def get_name(name_length):

        if name_length < 2:
            length = 2
        elif name_length > 40:
            length = 40
        else:
            length = name_length

        url = f"https://uzby.com/api.php?min={length}&max={length}"
        return requests.get(url).text

