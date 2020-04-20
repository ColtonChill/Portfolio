import sys

from Card import Card
from NumberSet import NumberSet


class Deck():
    def __init__(self, cardSize, cardCount, numberMax):
        """Deck constructor"""
        self.deck = []
        self.cardSize = cardSize
        self.cardCount = cardCount
        self.numberMax = numberMax
        for i in range(0, self.cardCount):
            self.deck.append(Card(i, self.cardSize, NumberSet(numberMax)))

    def getCardCount(self):
        """Return an integer: the number of cards in this deck"""
        return self.cardCount

    def getCard(self, n):
        """Return card N from the deck"""
        card = None
        n -= 1
        if 0 <= n < self.getCardCount():
            card = self.deck[n]
        return card

    def print(self, file=sys.stdout, idx=None):
        """void function: Print cards from the Deck

        If an index is given, print only that card.
        Otherwise, print each card in the Deck
        """
        if idx is None:
            for idx in range(1, self.cardCount + 1):
                c = self.getCard(idx)
                c.print(file)
            print('', file=file)
        else:
            self.getCard(idx).print(file)
