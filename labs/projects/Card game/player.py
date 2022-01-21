

from sqlalchemy import false, true
from card import Card


class Player:

    def __init__(self, name) -> None:
        self.name = name
        self.cards = []

    def add_card(self, card:Card):
        self.cards.append(card)
    
    def add_cards(self, cards:list):
        for card in cards:
            self.add_card(card)
    
    def show(self):
        for card in self.cards:
            card.show()
    
    def draw(self):
        return self.cards.pop(0)

    def hasCards(self):
        if len(self.cards) > 0:
            return True
        else:
            return False

    def battle(self, other):
        card_self = self.draw()
        card_other = other.draw()
        won_cards = []

        while card_self.isEqual(card_other) and self.hasCards() and other.hasCards():
            won_cards.append(card_self)
            won_cards.append(card_other)
            for i in range(0, 3):
                if len(self.cards) > 1 and len(other.cards) > 1:
                    won_cards.append(self.draw())
                    won_cards.append(other.draw())
            card_self = self.draw()
            card_other = other.draw()

        won_cards.append(card_self)
        won_cards.append(card_other)

        if card_self.isGreater(card_other):
            self.add_cards(won_cards)
        else:
            other.add_cards(won_cards)