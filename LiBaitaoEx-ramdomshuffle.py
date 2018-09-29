from random import randint
oldDeck = ['a','b','c','d','e']
newDeck = []
while len(oldDeck)>0:
    n = randint(0,len(oldDeck)-1)
    newDeck = newDeck + [oldDeck[n]]
    oldDeck.pop(n)
