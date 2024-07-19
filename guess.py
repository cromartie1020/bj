from random import randint
print("Please think of a number between 0 and 100")
  
number = randint(0,100)
selected = 'h'
high = 100
low  = 0

while selected != 'c':
    if number > (int((high + low)/2)):
        low = int((high + low)/2)
        print('Is your secret number: ' + str(low) + '?' )
        print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. " , 'l')
         
         
    elif number <  (int ((high + low)/2)): 
        high = int((high + low)/2)
        print('Is your secret number: ' + str(high) + '?')
        print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ", 'h')
        
    else:
        selected = 'c'
        guess = int((high + low)/2)
        print('Is your secret number: ' + str(guess) + '?')
        print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ", 'c')
        print('Your number is ' + str(guess) + '.')
        


              
    
