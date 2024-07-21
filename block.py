test = 'dddefg'  
def choice():
    name = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. " )
    
    if name == 'l' or name == 'h' or name == 'c':
        test = 'abcd-/kl;lv'
        return name,  test
    else:
        print('Sorry, I do not understand that.'  )
        test = False  
        return name, test    
            
while test != 'abcd-/kl;lv':          
    name, test=choice()
    
