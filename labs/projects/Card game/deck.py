import random

from sqlalchemy import null
from card import Card

class Deck:

    suits = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
    
    def __init__(self) -> None:
        self.cards = []
        for suit in Deck.suits:
            for value in range(2, 15):
                self.cards.append(Card(suit, value))
        self.shuffle()

    def show(self) -> str:
        for card in self.cards:
            card.show()

    def deal_card(self):
        return self.cards.pop()
    
    def deal_start(self, player1, player2):
        while len(self.cards) > 0:
            player1.add_card(self.deal_card())
            player2.add_card(self.deal_card())
       

    def shuffle(self):
        new_deck = []
        old_deck = list(self.cards)

        while len(new_deck) < 52:
            index = random.randint(0,51)
            if old_deck[index] != 'null':
                new_deck.append(old_deck[index])
                old_deck[index] = 'null'

        self.cards = new_deck