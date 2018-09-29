from collections import namedtuple
Card = namedtuple('Card', ['value', 'suit'])
suits= ['hearts', 'diamonds', 'spades', 'clubs']
cards = [Card(Value, suit) for value in range(1,14) for suit in suits]
print(cards[0])
print(cards[0].value, card[0].suit)
