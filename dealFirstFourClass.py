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
    def top_of_deck(self):                       #This function returns the top of the deck card.
        pop_value = self.temp.pop()
        return pop_value
    
    def four(self):                              # This function returns four cards from the top of the deck. 
        four_cards=[]
        four_cards.append(self.temp.pop())
        four_cards.append(self.temp.pop())
        four_cards.append(self.temp.pop())
        four_cards.append(self.temp.pop())
        
        return four_cards
    
        
        
     
         
        
# testing the class    
cards=Shuffle(temp)
temp=cards.random_cards()
print(temp)
pop_value=cards.top_of_deck()
print(pop_value)
print(temp)
pop_value=cards.top_of_deck()
print(pop_value)
print(temp)
list_four=cards.four()
print(list_four)
print(temp)