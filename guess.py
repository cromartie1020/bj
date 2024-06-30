from random import randint
print("Please think of a number between 0 and 100")
 
number = randint(0,100)
selected = None
high = 100
low  = 0
while selected != 'c':
    print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly."))
    if number > int((high + low)/2):
        print('Is your secret number ' + str(number) + '?' )
        print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly."))
        high = 
        low  = 
    elif number < int ((high + low)/2):
        print('Is your secret number' + str(number))
        print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly."))
        
    else:
        


              
    
