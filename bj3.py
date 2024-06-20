from random import choice
#from black_jack import ace_hand, choose_card, shuffle, winner,busted,temp,hit,dealer_hit
with open('blackjack.txt', 'w+') as bj:
    config=bj.readlines()
    
count=0
count_11 = 0    
dealer_count=0
dealer_count11=0
bet=1
balance=100
global toggle
toggle = True
def choose_card():
    '''
    Selected card in order is heart, spade, diamond, club.
    52//4 for the number card then add the type of card to
    the number card. If card_type == 0 then it is a heart.
    If card_type == 1 then it is a spade etc... 
    '''
    selected_card=temp.pop()
    card_number = selected_card//4
    print('card_number: ',card_number)
    card_type= selected_card - 4*card_number
    print('New card selected and the new length of temp: ',len(temp)) 
    if card_type==0:
        card_type='Heart'
    elif card_type==1:
        card_type='Spade'
    elif card_type==2:
        card_type='Diamond'
    elif card_type==3:
        card_type='Club'    
    
    return card_number, card_type, temp
def dealer_hit(count, count11,dealer_count,dealer_count11):
    global card
    toggle= False
    print(temp)
    print('Dealer hand called.')
    #if dealer_count < 17 and dealer_count > 0 and dealer_count11 <17:
    #    hit(count, balance=0,bet=0, dealer_count11 )
    #elif dealer_count < 22:
    #    if count < dealer_count or count < dealer_count11:
    #        print('Dealer lost') 
    print('dealer_count before < 17 ',dealer_count)
    if count < dealer_count and dealer_count > 16:
        print ('Dealer Wins dealer has: ', dealer_count  )
        
           
        selected=input('Play again? Y/N ')
        if selected.lower()=='y':
            deal()
            return selected    
        else:
            quit()   
        
    while dealer_count<17 and toggle == False:
        print('Dealer has: ',dealer_count)
        card   =choose_card()
        card = int(card[0])
        
        print('card',type(card),'dealer_count',type(dealer_count))
        dealer_count += card
        dealer_hit(count,count11,dealer_count,dealer_count11)
        print(dealer_count, count, count11,dealer_count11 )
        if dealer_count > 21:
            print('dealer_count dealer is busted the dealer has. ',dealer_count)
        selected =input( 'Do you wish to play again y/n: ')
        selected = selected.lower()
        if selected == 'y':
            deal()
        else:
            toggle = True 
        selected = selected.lower()
        if selected == 'y':
            quit()
        if selected == 'n':
            quit()
        if dealer_count == count:
            print('Push')
        if dealer_count > count:
            print ('Dealer Wins')
            print(temp)
        if dealer_count < count and dealer_count < 21:
            print ('Player Wins', temp)

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
    if player_hand <8 and player_hand1<8 :
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
    
def winner(player='player'):
    print('Player won')
    deal()
    
def player():
    pass

#def dealer(count,count_11,dealer_count,dealer_count11,  balance,bet=0):

    
def deal():
    '''
    Deal two cards to the player and dealer an alternating cards.
    has to give him/her the option to hit, double down, stay, split, or
    if he/she has blackjack.
    '''
    deposit=100
    count_11=0
    dealer_count11=0
    player_hand, card_type, temp = choose_card()
    dealer_hand, card_type, temp = choose_card()
    player_hand1, card_type, temp = choose_card()
    dealer_hand1, card_type, temp = choose_card()
    
    if player_hand > 9:
        player_hand = 10
    if player_hand1>9:
        player_hand1=10
    print('player_hand :',player_hand,'player_hand1:', player_hand1)
    if player_hand ==1 or player_hand1==1:   #This means both cards are aces.
        count,count_11, player_hand,  player_hand1 = ace_hand(player_hand, player_hand1)
        print('count: ',count, 'count_11: ',count_11,'player_hand: ',player_hand,'player_hand1: ', player_hand1)
    else:
        count= player_hand+player_hand1
    #-----------------------Dealer hand---------------------------------------------    
    if dealer_hand > 9:
        dealer_hand = 10
    if dealer_hand1>9:
        dealer_hand1=10
    if dealer_hand ==1 or dealer_hand1 ==1: # This means both dealer cards are aces. 
        dealer_count, dealer_count11,dealer_hand,  dealer_hand1 =ace_hand(dealer_hand, dealer_hand1)
    dealer_count =dealer_hand+ dealer_hand1
    
    
    print('player_count : ',count,'player_count_11: ',count_11, 'dealer_count: ',dealer_count, 'dealer_count11: ',dealer_count11)
    if count_11 == 21 and dealer_count11 !=21:
        # Player wins if dealer_count11 does not equal 21.
        winner()
        selected = input ('Do  you wish to play again? Y/n')
        selected = selected.lower
        if selected == 'n':
            quit()
        else:
            deal()
    # The two player cards are the same.
    if player_hand == player_hand1:
        print('Hit','Split','Double Down','Stand')
             # The player does not have 21 and the cards are of different values.
    toggle=True
    while toggle:
        selected=input('Hit: H - Double Down: D - Stand: S ')
        selected.lower()
        if selected.lower()=='s':
            print('Player Count: ',count)
            # Call dealer_hit function
            dealer_hit(count,count_11,dealer_count,dealer_count11)
            toggle=False
           
        if selected.lower() == 'h' and count < 21:
            count=hit(count,100,10,count_11)
            print(count)   # For some reason the count does not print
            if count == 21:
                winner('player')
                #deal()
            if count >21:
                # Game is over and player lost.
                
                print('busted')
                play=input('Do you wish to play another hand y/n: ')
                play = play.lower()
                if play=='n':
                    toggle=False
                else:    
                    deal()
                  
                
    #-----------------------Dealer Hand----------------------------------------
    '''
    Dealer must hit when dealer_count is 16 or less. Dealer must stay if total
    is 17 or greater. If dealer_hand1 is an ace then the player is offer insur-
    ance. If dealer has 21 on first two cards and player does not have 21 on first
    two cards player looses and bet is deducted from total.
    ''' 
    return player_hand, dealer_hand, player_hand1, dealer_hand1

while toggle:
    deal()
