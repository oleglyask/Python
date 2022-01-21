

from xmlrpc.client import boolean




class Card:

    def __init__(self, suit, value) -> None:
        self.suit = suit
        self.value = value

    def show(self) -> str:
        print(f'{self.value} of {self.suit}')

    def isEqual(self, other) -> boolean:
        if self.value == other.value:
            return True
        else:
            return False
    
    def isGreater(self, other) -> boolean:
        if self.value > other.value:
            return True
        else:
            return False
