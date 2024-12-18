import sys, os
from random import choice
temp=[]
def shuffle():
    os.system('clear')
    
    cards = [card for card in range(1,53)]
    while len(cards)!= 0:
        selected=choice(cards)                              # Selects a random card.
        temp.append(selected)                               # Append that card to temp. 
        cards.remove(selected)                              # Now remove the selected card from cards. 
    global play_count
    play_count=0

    return temp

temp=shuffle()
print(temp)
card=temp.pop()
print (card)
print(temp)