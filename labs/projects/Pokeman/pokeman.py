# - Each Pokemon should have a `name`, `primary_type`, `max_hp` and `hp`
# - Primary types should be limited to `water`, `fire` and `grass`
# - Implement a `battle()` method based on rock-paper-scissors that
#   decides who wins based only on the `primary_type`:
#       water > fire > grass > water
# - Display messages that explain who won or lost a battle
# - If a Pokemon loses a battle, they lose some of their `hp`
# - If you call the `feed()` method on a Pokemon, they regain some `hp`


import random

class Pokeman:

    primary_types = ['water', 'fire', 'grass']

    def __init__(self, name, max_hp) -> None:
        self.name = name
        self.primary_type = random.choice(Pokeman.primary_types)
        self.max_hp = max_hp
        self.hp = max_hp

    def __str__(self) -> str:
        return f"name: {self.name}\nprimary type: {self.primary_type}\nmax hp: {self.max_hp}\nhp: {self.hp}\n"

    def loose_hp(self):
        self.hp -= 10

    def battle(self, other):

        print(f"{self.name}({self.primary_type}) battles {other.name}({other.primary_type})")
        
        result_map = {0: 'loose', 1: 'win', -1: 'tie'}
        battle_key = {'water': 0, 'fire': 1, 'grass': 2}
        result_hash = [
            [-1, 1, 0],
            [0, -1, 1],
            [1, 0, -1]
        ]

        result = result_hash[battle_key[self.primary_type]][battle_key[other.primary_type]]

        print(f"{self.name} {result_map[result]}")