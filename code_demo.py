import sys,os
from random import choice
card=[1,2,3,4]

temp=[]

def shuffle():
    os.system('clear')
    
    cards = [card for card in range(1,53)]
    while len(cards)!= 0:
        selected=choice(cards)                              # Selects a random card.
        temp.append(selected)                               # Append that card to temp. 
        cards.remove(selected)                              # Now remove the selected card from cards. 
       
    
    return temp

temp=shuffle()
print(temp)