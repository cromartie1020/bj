from random import choice
import sys,os
temp=[]
first_four_cards=[]
def shuffle():
    '''
    Shuffles the deck of 52 cards.
    Uses the imported random choice. 
    first_four_cards variable holds the random
    first 4 cards poped from deck of cards.  
    '''
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
for x in range(0,4):
    hold = temp.pop()
    first_four_cards.append(hold)
    

