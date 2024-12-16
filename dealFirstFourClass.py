from random import choice
import sys,os
temp=[]
first_four=[]
class Shuffle:

    '''
    Shuffles the deck of 52 cards.
    Uses the imported random choice. 
    first_four_cards variable holds the random
    first 4 cards poped from deck of cards.
    Requires a random list of 52 cards and a list
    to hold four cards.
    Must import sys and os.   
    '''
    def __init__(self,temp,first_four):
        self.temp=temp
        self.first_four=first_four
    
    def clear(self):
        os.system('clear')
    def random_cards(self):
        cards=[]
        cards = [card for card in range(1,53)]
        while len(temp)!= 0:
            selected=choice(temp)                              # Selects a random card.
            cards.append(selected)                         # Now remove the selected card from cards. 
    global play_count
    play_count=0

    return temp
temp=shuffle()
for x in range(0,4):
    hold = temp.pop()
    first_four_cards.append(hold)
    

