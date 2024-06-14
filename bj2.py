from black_jack import ace_hand, choose_card, shuffle, winner,busted,temp,hit,dealer_hit
with open('blackjack.txt', 'w+') as bj:
    config=bj.readlines()
    
count=0
count_11 = 0    
dealer_count=0
dealer_count11=0
bet=1
balance=100
toggle = True
    
def deal():
    '''
    Deal two cards to the player and dealer an alternating cards.
s    has to give him/her the option to hit, double down, stay, split, or
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
    # This is my first set of hands    
    print('player_hand :',player_hand,'player_hand1:', player_hand1)
    if player_hand == 1 and player_hand1 == 1:   #This means both cards are aces.
        count = 2        # Two aces means the count is equal to 2 and count_11 equal 12 
        count_11 = 12
        #count,count_11, player_hand,  player_hand1 = ace_hand(player_hand, player_hand1)
        print('count: ',count, 'count_11: ',count_11,'player_hand: ',player_hand,'player_hand1: ', player_hand1)
    elif player_hand == 1:   #This means one card is an ace.   
        count= player_hand+player_hand1
        count_11=11+player_hand1
    elif player_hand1 == 1:
        count = player_hand + player_hand1
        count_11= 11 + player_hand
    else:
        count = player_hand + player_hand1
        count_11 = 0
    #-----------------------Dealer hand---------------------------------------------    
    if dealer_hand > 9:
        dealer_hand = 10
    if dealer_hand1>9:
        dealer_hand1=10
        
    if dealer_hand ==1 and dealer_hand1 ==1: # This means both dealer cards are aces. 
        dealer_count, dealer_count11,dealer_hand,  dealer_hand1 =ace_hand(dealer_hand, dealer_hand1)
    dealer_count =dealer_hand+ dealer_hand1
    #dealer_count = dealer_hand + dealer_hand1
    
    print('player_count : ',count,'player_count_11: ',count_11, 'dealer_count: ',dealer_count, 'dealer_count11: ',dealer_count11)
    if count_11 == 21 and dealer_count11 !=21:
        # Player wins if dealer_count11 does not equal 21.
        winner()
        
        selected = input("Would you like to continue Y/N")
        selected = selected.lower()
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
        selected=input("Hit: H - Double Down: D - Stand: S ")
        selected.lower()
        if selected.lower()=='s':
            print('Player Count: ',count)
            # Call dealer_hit function
            dealer_hit(count,count_11,dealer_count,dealer_count11)
            selected = input('Do you wish to play another hand? Y/n? ') 
            selected=selected.lower()
            if selected == 'y':
                deal()
           
        if selected.lower() == 'h' and count < 21:
            count=hit(count,100,10,count_11)
            print(count)   # For some reason the count does not print
            if count == 21:
                winner('player')
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
    
deal()
