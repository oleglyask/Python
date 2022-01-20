# Build a very basic Pokémon class that allows you to simulate battles
# in a Rock-Paper-Scissors game mechanic, as well as feed your Pokémon.
#
# The class should follow these specifications:
#

from pokeman import Pokeman

player1 = Pokeman('Picacho',10)
player2 = Pokeman('computer', 50)

player1.battle(player2)
