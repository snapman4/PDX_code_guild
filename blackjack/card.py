class Card:
    def __init__(self, suit, rank, value=0):
        self.suit = suit
        self.rank = rank
        self.value = value #can be none but in this case we don't want it to be zero

    def __str__(self):
        return '{} of {}'.format(self.rank, self.suit)

    def __repr__(self):
        return '{}-{}'.format
if __name__ == '__main__':
    c1 = Card('Hearts', 'Ace', 1)
    print(c1)