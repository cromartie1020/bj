from random import choice
import sys,os
temp=[]
first_four=[]
play_count=0
class Shuffle:

    '''
    The calling function requires two list.
    def __init__(self,temp,first_four)

    Shuffles the deck of 52 cards.
    Uses the imported random choice. 
    first_fourcleearf variable holds the random
    first 4 cards poped from deck of cards.
    Requires a random list of 52 cards and a list
    to hold four cards.
    Must import sys and os.   
    '''
    
    def __init__(self,temp,first_four=[]):
        self.temp=temp
        self.first_four=first_four
    
    def clear(self):
        os.system('clear')
    def random_cards(self):
        
        cards = [card for card in range(1,53)]
        
        while len(cards)!= 0:
            selected=choice(cards)                              # Selects a random card.
            temp.append(selected)
            cards.remove(selected)                         # Now remove the selected card from cards. 
            
            
        return temp
    def four(self):
        
        for  x in range(0,4):

            selected = temp.pop()
            first_four.append(selected)
        return first_four    
            
# Test the class   
'''         
first=Shuffle(temp, first_four)

temp=first.random_cards()
print ('temp:', temp)
first_four = first.four()



print(first_four)
'''



    

