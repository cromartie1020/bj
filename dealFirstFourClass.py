from random import choice
import sys,os
temp=[]
first_four=[]
play_count=0
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
    
    def __init__(self,temp,first_four=[]):
        self.temp=temp
        self.first_four=first_four
    
    def clear(self):
        os.system('clear')
    def random_cards(self):
        
        cards = [card for card in range(1,53)]
        while len(self.temp)!= 0:
            selected=choice(temp)                              # Selects a random card.
            cards.append(selected)                         # Now remove the selected card from cards. 
            temp[selected].delete 
            
        return cards
    def four(self):
        
        cards=[]
        for  x in range(0,4):

            hold = temp.pop()
            cards.append(hold)
            if x == 3:
                return first
            
# Test the class            
first=Shuffle(temp, first_four)
temp=first.random_cards()
first_four = first.four()
'''
for x in range(0,4):
    hold = temp.pop()
    first_four.append(hold)
'''
print(Shuffle(help))
print(help(Shuffle))
print (temp)
print(first_four)




    

