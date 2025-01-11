card_number = 0
card_ace    = 0
card_suit={1:'ACE HEARTS',2:'ACE SPADES',3:'ACE DIAMONDS',4:'ACE CLUBS',\
    5:'2 of HEARTS',6:'2 of SPADES', 7:'2 of DIAMONDS',8:'2 of CLUBS',\
    9:'3 of HEARTS',10:'3 of SPADES', 11:'3 of DIAMONDS',12:'3 of CLUBS',\
    13:'4 of HEARTS',14:'4 of SPADES', 15:'4 of DIAMONDS',16:'4 of CLUBS',\
    17:'5 of HEARTS',18:'5 of SPADES', 19:'5 of DIAMONDS',20:'5 of CLUBS',\
    21:'6 of HEARTS',22:'6 of SPADES', 23:'6 of DIAMONDS',24:'6 of CLUBS',\
    25:'7 of HEARTS',26:'7 of SPADES', 27:'7 of DIAMONDS',28:'7 of CLUBS',\
    29:'8 of HEARTS',30:'8 of SPADES', 31:'8 of DIAMONDS',32:'8 of CLUBS',\
    33:'9 of HEARTS',34:'9 of SPADES', 35:'9 of DIAMONDS',36:'9 of CLUBS',\
    37:'10 of HEARTS',38:'10 of SPADES', 39:'10 of DIAMONDS',40:'10 of CLUBS',\
    41:'JACK of HEARTS',42:'JACK of SPADES', 43:'JACK of DIAMONDS',44:'JACK of CLUBS',\
    45:'QUEEN of HEARTS',46:'QUEEN of SPADES', 47:'QUEEN of DIAMONDS',48:'QUEEN of CLUBS',\
    49:'KING of HEARTS',50:'KING of SPADES', 51:'KING of DIAMONDS',52:'KING of CLUBS'                
}   

if card_suit>0 and card_suit < 5:
    card_number = 1
    card_ace    = 11
if card_suit>4 and card_suit < 9:
    card_number = 2
if card_suit>8 and card_suit < 13:
    card_number = 3
if card_suit>12 and card_suit < 17:
    card_number = 4
if card_suit> 16 and card_suit < 21:
    card_number = 5
if card_suit>20 and card_suit < 25:
    card_number = 6
if card_suit>24 and card_suit < 29:
    card_number = 7
if card_suit>28 and card_suit < 33:
    card_number = 8
if card_suit>32 and card_suit < 37:
    card_number = 9
if card_suit>36 and card_suit < 53:
    card_number = 10
    
    
    
        
        
    


     

