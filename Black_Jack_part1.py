
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

class Cards():
    
    #This is the initialization of the class
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
    
    #This is the method for printing the individual card
    def __str__(self):
        return f"{self.rank} of {self.suit}"

#Stores created cards
class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Cards(rank,suit))
    
    def __str__(self):
        for card in self.deck:
            print (f"{card}")
        return ""

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        pass