from random import randint
print("Please think of a number between 0 and 100")
epsilon = 0  
number = randint(0,100)
selected = 'h'
high = 100
low  = 0
number = 1
while selected != 'c':
    print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if number > (int((high + low)/2)):
        low = int((high + low)/2)
        print('Is your secret number: ' + str(low) + '?' )
        print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
        epsilon = number - low
        if epsilon == 1:
            print('Your number is ', str(low) + '.')
        
        print ('h') 
         
    elif number <  (int ((high + low)/2)): 
        high = int((high + low)/2)
        print('Is your secret number: ' + str(high) + '?')
        print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
        print('l')
        epsilon = high - number
        if epsilon == 1:
            print ('Your number is ', int(high)) 
    else:
        selected = 'c'
        guess = int((high + low)/2)
        print(number,guess)
        


              
    
