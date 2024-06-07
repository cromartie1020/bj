from black_jack import ace_hand, choose_card, shuffle, hit

count=0
count_11 = 0    
dealer_count=0
dealer_count11=0
balance = 100.00
bet=5

    
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
    dealer_count=dealer_hand+dealer_hand1
    dealer_count = dealer_hand + dealer_hand1
    
    print('player_count : ',count,'player_count_11: ',count_11, 'dealer_count: ',dealer_count, 'dealer_count11: ',dealer_count11)
    # The two player cards are the same.
    if player_hand == player_hand1:
        print('Hit','Split','Double Down','Stand')
        selected_option=input('Input S for Split,H for Hit, D for Double Down, Z for Stay: ')
        selected_option=selected_option.lower()
        if selected_option=='h':
            hit(count, balance, bet, count_11)
        
    # The player does not have 21 and the cards are of different values.    
    elif count < 21:
        print('Hit',',' ,' Double Down',',', ' Stand')
        selected_option=input('Input,H for Hit, D for Double Down, S for Stay: ')
        selected_option=selected_option.lower()
        if selected_option=='h':
            hit(count, balance, bet, count_11)
    return player_hand, dealer_hand, player_hand1, dealer_hand1
    
deal()
