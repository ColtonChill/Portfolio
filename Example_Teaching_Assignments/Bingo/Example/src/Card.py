import sys

from NumberSet import NumberSet

class Card():
    def __init__(self, idnum, size, numberSet):
        """Card constructor"""
        self.id = idnum
        self.size = size
        numberSet.randomize()
        self.numberSet = numberSet

    def getId(self):
        """Return an integer: the ID number of the card"""
        return self.id

    def getSize(self):
        """Return an integer: the size of one dimension of the card.
        A 3x3 card will return 3, a 5x5 card will return 5, etc.
        """
        return self.size

    def print(self, file=sys.stdout):
        """void function:
        Prints a card to the screen or to an open file object"""
        file.write(f"Card #{self.id+1} \n")
        file.write("+")
        free = False
        if self.size % 2 == 1:
            free = True
        for j in range(self.size):
            file.write("-----+")
        file.write("\n")
        for i in range(self.size):
            file.write("|")
            for j in range(self.size):
                if free and i == int(self.size/2) and j == int(self.size/2):
                    file.write("{:^5}|".format("FREE!"))
                else:
                    file.write("{:^5}|".format(self.numberSet.getNext()))
            file.write("\n+")
            for j in range(self.size):
                file.write("-----+")
            file.write("\n")
        file.write("\n")
