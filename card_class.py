from dealFirstFourClass import temp


suit={1:'ACE HEARTS',2:'ACE SPADES',3:'ACE DIAMONDS',4:'ACE CLUBS',\
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

card_value=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20\
    ,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,\
        40,41,42,43,44,45,46,47,48,49,50,51,52]


card_value=temp.pop()
card_ace = 0
card_number=0
card_ace1=0
               
class determine_card:
    def __init__(self, card_value, suit='ACE OF HEARTS',card_number=1,card_ace=0, card_ace1=0):
        self.suit=suit
        self.card_value=card_value
        self.card_number=1
        self.card_ace = 0
        self.card_ace1=0
     
    def card_type(self):
        if  self.card_value == 1:
            self.suit = 'ACE OF HEARTS'
            self.card_number= 1
            self.card_ace =  11
            self.card_ace1=1
            
        elif card_value == 2:
            self.suit = 'ACE OF SPACES'
            self.card_number= 1
            self.card_ace =  11   
            self.card_ace1=1   
        elif card_value==3:
            self.suit = 'ACE OF DIAMONDS'
            self.card_number = 1
            self.card_ace = 11   
            self.card_ace1=1  
        elif self.card_value==4:
            self.suit = 'ACE OF CLUBS'
            self.card_number = 1
            self.card_ace = 11
            self.card_ace1=1
        elif self.card_value==5:
            self.suit = '2 OF HEARTS'
            self.card_numbewr = 2
        elif self.card_value==6:
            self.suit = '2 OF SPADES'
            self.card_number = 2
        elif self.card_value==7:
            self.suit = '2 OF DIAMONDS'
            self.card_number = 2
        elif self.card_value==8:
            self.suit = '2 OF CLUBS'
            self.card_number = 2
        elif self.card_value==9:
            self.suit = '3 OF HEARTS'
            self.card_number = 3
        elif self.card_value==10:
            self.suit = '3 OF SPADES'
            self.card_number = 3
        elif self.card_value==11:
            self.suit = '3 OF DIAMONDS'
            self.card_value = 3
        elif self.card_value==12:
            self.suit = '3 OF CLUBS'
            self.card_number = 3
        elif self.card_value==13:
            self.suit = '4 OF HEARTS'
            self.card_number = 4
        elif self.card_value==14:
            self.suit = '4 OF SPADES'
            self.card_number = 4
        elif self.card_value==15:
            self.suit = '4 OF DIAMONDS'
            card_number = 4
        elif card_value==16:
            self.suit = '4 OF CLUBS'
            card_number = 4
        elif self.card_value==17:
            self.suit = '5 OF HEARTS'
            self.card_number = 5
        elif card_value==18:
            self.suit = '5 OF SPADES'
            self.card_number = 5
        elif self.card_value==19:
            self.suit = '5 OF DIAMONDS'
            self.card_number = 5
        elif self.card_value==20:
            self.suit = '5 OF CLUBS'
            self.card_number = 5
            
        elif self.card_value==21:
            self.suit = '6 OF HEARTS'
            self.card_number = 6
        elif self.card_value==22:
            self.suit = '6 OF SPADES'
            self.card_number = 6
        elif self.card_value==23:
            self.suit = '6 OF DIAMONDS'
            self.card_number = 6
        elif self.card_value==24:
            self.suit = '6 OF CLUBS'
            self.card_number = 6

        elif self.card_value==25:
            self.suit = '7 OF HEARTS'
            self.card_number = 7
        elif self.card_value==26:
            self.suit = '7 OF SPADES'
            self.card_number = 7
        elif self.card_value==27:
            self.suit = '7 OF DIAMONDS'
            self.card_number = 7
        elif self.card_value==28:
            self.suit = '7 OF CLUBS'
            self.card_number = 7
            
        elif self.card_value==29:
            self.suit = '8 OF HEARTS'
            self.card_number = 8
        elif self.card_value==30:
            suit = '8 OF SPADES'
            card_number = 8
        elif self.card_value==31:
            self.suit = '8 OF DIAMONDS'
            self.card_number = 8
        elif self.card_value==32:
            self.suit = '8 OF CLUBS'
            self.card_number = 8
            
        elif self.card_value==33:
            self.suit = '9 OF HEARTS'
            self.card_number = 9
        elif self.card_value==34:
            self.suit = '9 OF SPADES'
            self.card_number = 9
        elif self.card_value==35:
            self.suit = '9 OF DIAMONDS'
            self.card_number = 9
        elif self.card_value==36:
            self.suit = '9 OF CLUBS'
            self.card_number = 9
            
        elif self.card_value==37:
            self.suit = '10 OF HEARTS'
            self.card_value = 10
        elif self.card_value==38:
            self.suit = '10 OF SPADES'
            self.card_number = 10
        elif self.card_value==39:
            self.suit = '10 OF DIAMONDS'
            self.card_number = 10
        elif self.card_value==40:
            self.suit = '10 OF CLUBS'
            self.card_number = 10
            
        elif self.card_value==41:
            self.suit = 'JACK OF HEARTS'
            self.card_number = 10
        elif self.card_value==42:
            self.suit = 'JACK OF SPADES'
            self.card_number = 10
        elif self.card_value==43:
            self.suit = 'JACK OF DIAMONDS'
            self.card_number = 10
        elif self.card_value==44:
            self.suit = 'JACK OF CLUBS'
            self.card_numbewr = 10
            
        elif self.card_value==45:
            self.suit = 'QUEEN OF HEARTS'
            self.card_number = 10
        elif self.card_value==46:
            self.suit = 'QUEEN OF SPADES'
            self.card_number = 10
        elif self.card_value==47:
            self.suit = 'QUEEN OF DIAMONDS'
            self.card_number = 10
        elif self.card_value==48:
            self.suit = 'QUEEK OF CLUBS'
            self.card_number = 10
            
        elif self.card_value==49:
            self.suit = 'KING OF HEARTS'
            self.card_number = 10
        elif self.card_value==50:
            self.suit = 'KING OF SPADES'
            self.card_number = 10
        elif self.card_value==51:
            self.suit = 'KING OF DIAMONDS'
            self.card_number = 10
        elif self.card_value==52:
            self.suit = 'KING OF CLUBS'
            self.card_number = 10
            
        return self.card_value, self.suit, self.card_number ,self.card_ace,self.card_ace1       

template=determine_card(card_value,suit, card_number,card_ace,card_ace1) 
card_value,card_suit,card_number,card_ace,card_ace1=template.card_type()
    

