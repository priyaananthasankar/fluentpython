import collections
Card = collections.namedtuple('Card',['rank','suit'])

class CardDeck:

    ranks = [n for n in range(2,11)] + list('AKJQ')
    suits = "spade diamond heart club".split()

    def __init__(self):
        self._cards = [Card(r,s) for r in self.ranks for s in self.suits]

    def __getitem__(self,position):
        return self._cards[position]
    
    def __len__(self):
        return len(self._cards)

deck = CardDeck()

# Len calls the internal dunder len
print(len(deck))

# iterable
for item in deck:
    print(item)

print("*" * 10)

# Pick out a position
print(deck[0])
print(deck[-1])

print("*" * 10)

# randomize
from random import choice
print(choice(deck))
print(choice(deck))

print("*" * 10)

# __contains__ does a sequential scan
print(Card("A","club") in deck)
print(Card("J","hearts") in deck)

# instead of len(suit_value) it could be any fixed multiplier that can render unique value
# if there is no multiplier there isnt a unique value per rank and ranks get mixed up
suit_value = dict(spade=3,diamond=2,heart=1,club=0)
def spades_high(card):
    rank_value = CardDeck.ranks.index(card.rank)
    return rank_value * len(suit_value) + suit_value[card.suit]

def my_key(card):
    return CardDeck.ranks.index(card.rank)

for card in sorted(deck,key=spades_high):
    print(card)
