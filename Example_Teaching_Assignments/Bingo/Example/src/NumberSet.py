import random


class NumberSet():
    def __init__(self, size):
        """NumberSet constructor"""
        self.size = size
        self.set = []
        self.index = 0
        for i in range(1, self.size+1):
            self.set.append(i)

    def getSize(self):
        """Return an integer: the size of the NumberSet"""
        return self.size

    def get(self, index):
        """Return an integer: get the number from this NumberSet at an index"""
        if index>=len(self.set) or index<0:
            return None
        return self.set[index]

    def randomize(self):
        """void function: Shuffle this NumberSet"""
        shuffled = []
        while len(self.set) > 0:
            r = random.randint(0, len(self.set) - 1)
            shuffled.append(self.set[r])
            self.set.remove(self.set[r])
        self.set = shuffled

    def getNext(self):
        """Return an integer: when called repeatedly return successive values
        from the NumberSet until the end is reached, at which time 'None' is returned"""
        if self.index >= self.size:
            return None
        else:
            self.index += 1
            return self.set[self.index-1]
