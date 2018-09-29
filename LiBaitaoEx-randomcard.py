from random import randint
deck = ['ac_hearts', 'ac_spades', 'ac_clubs', 'ac_diamonds', 'ki_hearts', 'ki_spades', 'ki_clubs', 'ki_diamonds','qu_hearts','qu_spades','qu_clubs','qu_diamonds','ja_hearts','ja_spades','ja_clubs','ja_diamonds','10_hearts','10_spades','10_clubs','10_diamonds','09_hearts','09_spades','09_clubs','09_diamonds','08_hearts','08_spades','08_clubs','08_diamonds','07_hearts','07_spades','07_clubs','07_diamonds','06_hearts','06_spades','06_clubs','06_diamonds','05_hearts','05_spades','05_clubs','05_diamonds','04_hearts','04_spades','04_clubs','04_diamonds','03_hearts','03_spades','03_clubs','03_diamonds','02_hearts','02_spades','02_clubs','02_diamonds']
numcards = 0
hand = []
#numcards should add up to 5
while numcards < 5:
    x = randint(0,51-numcards)
    hand.append(deck[x])
    deck = deck[:x] + deck[x+1:]
    numcards += 1
print(hand)
    
