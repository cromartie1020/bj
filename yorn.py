import os
def select():
    selected = True
    while selected:
        selected = input('Play another game(y/n): ')
        selected = selected.lower()
        if selected=='y':
            os.system('clear')
            return 'y'
        
        if selected=='n':
            quit()
            
        else:
            
            selected = True
            
      