from random import choice
from card import suit,determine_card,card_value
import sys,os
temp=[]

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
    
    def __init__(self,temp):
        self.temp=temp
        
    def clear(self):
        os.system('clear')
    def random_cards(self):                      #This funtion returns a 52 card deck.
        
        cards = [card for card in range(1,53)]
        
        while len(cards)!= 0:
            selected=choice(cards)
            self.temp.append(selected)
            cards.remove(selected)
            
        return temp    
    def first_four(self):
        pass     
        
# testing the class    
cards=Shuffle(temp)
temp=cards.random_cards()
print(temp)
