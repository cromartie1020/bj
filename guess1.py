#from random import randint
number = int(input("Please think of a number between 0 and 100: "))
      
selected = 'h'
high = 100
low  = 0
name = False
test = 'dddefg'  
def choice():
    name = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. " )
    
    if name == 'l' or name == 'h' or name == 'c':
        test = 'abcd-/kl;lv'
        return name,  test
    else:
        print('Sorry, I do not understand your input.'  )
        test = False  
        return name, test    
            


while selected != 'c':
    if number > (int((high + low)/2)):
        low = int((high + low)/2)
        print('Is your secret number ' + str(low) + '?' )
        while test != 'abcd-/kl;lv':          
            name, test=choice()
        test = 'dddefg'    
         
         
         
    elif number <  (int ((high + low)/2)): 
        high = int((high + low)/2)
        print('Is your secret number ' + str(high) + '?')
        while test != 'abcd-/kl;lv':          
            name, test=choice()
        test = 'abcdef'    

    elif number == (int ((high + low)/2)):
        guess = int((high + low)/2)
        print('Is your secret number ' + str(guess) + '?')
        while test != 'abcd-/kl;lv':          
            name, test=choice()
        test = 'dddefg'    
        print('Game over. Your secret number was: ' + str(guess) )
        selected = 'c'

              
    
