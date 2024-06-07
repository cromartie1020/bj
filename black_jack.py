from random import choice

global balance
balance = 100.00
def shuffle():
    temp=[]
    cards = [card for card in range(4,56)]
    while len(cards)!= 0:
        selected=choice(cards)
        temp.append(selected)
        cards.remove(selected)
    print('After shuffle: ',temp, 'length of temp: ',len(temp ))
    return temp
temp=shuffle()
def ace_hand(player_hand, player_hand1):
    count = 0
    count_11=0
    #dealer_count=0
    #
    dealer_count11=0    
    '''
    We need to count values when ace = 1 and ace = 11.
    count_11 is when ace = 11 and count is when ace =1.
    
    '''
    print('Either player_hand or player_hand1 is an ace.')
    if player_hand <5 and player_hand1<5 :
        #That means both cards are aces.
        count = 2
        count_11 = 12
        
             
    else:
        if player_hand == 1:
            count = 1+player_hand1
            count_11=11 + player_hand1
            toggle = True
        else:
            count = 1 + player_hand
            count_11 = 11 + player_hand
            toggle = False
        
    return count, count_11 ,player_hand,player_hand1

    
def hit(count, balance=0,bet=0, count_11=0):
    status = True
    new_card = temp.pop()
    
    new_card = new_card // 4
    if new_card >10:
        new_card=10
    count +=  new_card
    print('new_card: ', new_card, 'count: ', count)
    
    if count >21:
        balance -= bet
        status = False 
        print('busted')
        
        
    
    return count
    
def double_down(count,balance=0,bet=0,count_11=0):
    pass

def black_jack(count,balance=0,bet=0):
    pass
    
def split():
    pass
    
def busted():
    pass
    
def winner():
    pass
    
def player():
    pass

def dealer():        
    pass

def dealer_hand_count():
    pass
    
def player_hand_count():
    pass           



        



def choose_card():
    '''
    Selected card in order is heart, spade, diamond, club.
    52//4 for the number card then add the type of card to
    the number card. If card_type == 0 then it is a heart.
    If card_type == 1 then it is a spade etc... 
    '''
    selected_card=temp.pop()
    card_number = selected_card//4
    card_type= selected_card - 4*card_number
    if card_type==0:
        card_type='Heart'
    elif card_type==1:
        card_type='Spade'
    elif card_type==2:
        card_type='Diamond'
    elif card_type==3:
        card_type='Club'    
    
             
            
        
    return card_number, card_type, temp
