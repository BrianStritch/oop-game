import random

class Card(object):
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value
    
    def show(self):
       print( "{} of {}".format(self.value, self.suit))

class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()
    
    def build(self):
        for s in ['spades', 'Clubs', 'Diamonds', 'Hearts']:
            for v in range(1,14):
                self.cards.append(Card(s, v))
    
    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r= random.randint(0,i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i] 
    
    def drawCard(self):
        return self.cards.pop()

                


class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self

    def showHand(self):
        for card in self.hand:
            card.show()



# card = Card('Clubs', 6)

# card.show()

# deck.show()
# card2 = deck.draw()
# card2.show()
bob = Player('Bob')

deck = Deck()
deck.shuffle()

bob.draw(deck)
bob.showHand()


bob.drawCard(deck)
bob.showHand()
