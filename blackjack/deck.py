from blackjack_inclass import card
class Deck:
    RANK VALUE = {
        #create dictionary of ranks vaule 'ace': 1, '2': 2 etc...
    }
    SUITS = ['Diamonds', 'Hearts', 'Clubs', 'Spades']
    def __init__(self, number_decks=1):
        self.hopper = []
        self.number_decks = number_decks

    def generate_deck(self):
        decks = []
        for i in range self.number_decks:
            for s in self.Suits:    #s just stands for suit in this
                print (s)
                for r, v in self.RANK_VALUE.items():
                    decks.append(Card(s, r, v))
            return []

if __name__ == '__main__':
