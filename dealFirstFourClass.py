from random import choice
import sys,os
temp=[]
four=[]

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
    def random_cards(self):
        
        cards = [card for card in range(1,53)]
        
        while len(cards)!= 0:
            selected=choice(cards)
            self.temp.append(selected)
            cards.remove(selected)
            
        return temp    
    
    def first_four(self):
        for x in range (0,4):
            four.append(temp.pop())
        
        return four
        
             
        
# testing the class    
cards=Shuffle(temp)
cards.clear()
temp=cards.random_cards()

four=cards.first_four()

