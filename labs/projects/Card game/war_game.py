
# A game of cards where two players divide a deck and draw one card at a time. Player with the highest card takes both cards
# and places them on the bottom of the deck.  Game ends when one player has all the cards and wins

from deck import Deck
from player import Player

deck = Deck()
player1 = Player('Oleg')
player2 = Player('Computer')

deck.deal_start(player1, player2)

# print(f' player 1\n{len(player1.cards)}')
# print(f' player 2\n{len(player2.cards)}')

#  logic fails, gets stuck on even spit deck and goes back an forth
while (player1.hasCards() and player2.hasCards()):
    player1.battle(player2)

if player1.hasCards():
    print(f'{player1.name} won')
else:
    print(f'{player2.name} won')