from collections import namedtuple

# Creating a suit of cards using namedtuple
cd = namedtuple("CardDeck","suit name")
card_deck = []

suits = ["heart","spade","diamond","clubs"]
name = [i for i in range(2,11)] + list('AJQK')

# double for loop
card_deck = [cd(suit,n) for n in name for suit in suits]
print(card_deck)
s,n = card_deck[0]