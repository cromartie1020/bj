#from PIL import Image, ImageDraw, ImageFont
from tkinter import *

root = Tk()
e=Entry(root, bg='blue',fg='white')
e.grid(row=4,column=2,rowspan=50)


myLabel=Label(root, text=e.get() )
myLabel1=Label(root, text='Another note')

myLabel.grid(row=0, column=0)
myLabel1.grid(row=1, column=1)
#myLabel.grid1



def myClick():
    #myLabel1=Label(root,text='This is a test' ,fg='blue',bg='red');
    myLabel1 = Label(root, text=e.get())
    myLabel1.grid(row=3,column=2)
myButton=Button(root, text='Click me!', padx=50, pady=20, command=myClick,fg='blue',bg='green')
myButton.grid(row=2,column=2)


root.mainloop()
'''
root.iconbitmap('')

root.geometry('900x500')
root.configure(background='green')

my_frame=Frame(root, bg='green')
my_frame.pack(pady=20)

dealer_frame = LabelFrame(my_frame, text='Dealer',bd=0)
dealer_frame.grid(row=0, column=0, padx=20,ipadx=20)                  

player_frame = LabelFrame(my_frame, text='Player',bd=0)
player_frame.grid(row=0, column=1, ipadx=20)

dealer_label = Label(dealer_frame, text ='')
dealer_label.pack(pady=20)

player_label = Label(player_frame, text ='')
player_label.pack(padx=20)




root.mainloop()
'''