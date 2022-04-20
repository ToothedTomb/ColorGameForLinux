# import the modules 
import tkinter
from tkinter import CENTER, ttk, messagebox
from tkinter import Tk, Label, Button
import tkinter.messagebox
import random 
import os
from tkinter.ttk import *
import tkinter as tk
import sys




# list of possible colour. 
colours = ['Red','Blue','Green','Pink','Black', 
        'Yellow','Orange','White','Purple','Brown','Grey'] 
score = 1

# the game time left, initially 90 seconds. 
timeleft = 90

# function that will start the game. 
def startGame(event): 
    
    if timeleft == 90: 
        
        # start the countdown timer. 
        countdown() 
        
    # run the function to 
    # choose the next colour. 
    nextColour() 

# Function to choose and 
# display the next colour. 
def nextColour(): 

    # use the globally declared 'score' 
    # and 'play' variables above. 
    global score 
    global timeleft 

    # if a game is currently in play 
    if timeleft > 0: 

        # make the text entry box active. 
        e.focus_set() 

        # if the colour typed is equal 
        # to the colour of the text 
        if e.get().lower() == colours[1].lower(): 
            
            score += 1
        else:
            score -= 1

        # clear the text entry box. 
        e.delete(0, tkinter.END) 
        
        random.shuffle(colours) 
        
        # change the colour to type, by changing the 
        # text _and_ the colour to a random colour value 
        label.config(fg = str(colours[1]), text = str(colours[0])) 
        
        # update the points. 
        scoreLabel.config(text = "Points: " + str(score)) 


# Countdown timer function 
def countdown(): 

    global timeleft 

    # if a game is in play 
    if timeleft > 0: 

        # decrement the timer. 
        timeleft -= 1
        
        # update the time left label 
        timeLabel.config(text = "Time left: "
                            + str(timeleft)) 
                                
        # run the function again after 1 second. 
        timeLabel.after(1000, countdown) 


# Driver Code 

# create a GUI window 
root = tkinter.Tk() 

# set the title 
root.title("Color Game For FreeBSD 5.0!") 
root.tk.call('wm', 'iconphoto', root._w, tkinter.PhotoImage(file='ColorGameForLinux.png'))

# set the size 
root.geometry("820x640")
#Cant maximise the software!
root.resizable(0,0)
style = Style()
Help = tkinter.Label(root, text = "Color Game For FreeBSD 5.0!", font = ('Ubuntu', 24,"bold","underline")) 
                
Help.pack() 
# add a time left label 
timeLabel = tkinter.Label(root, text = "Time left " +
            str(timeleft), font = ('Ubuntu', 28)) 
                
timeLabel.pack() 
# add a score label 
scoreLabel = tkinter.Label(root, text = "Press enter to start:", 
                                    font = ('Ubuntu', 28)) 
scoreLabel.pack() 



# add a label for displaying the colours 
label = tkinter.Label(root, font = ('Ubuntu', 170)) 
label.pack() 

# add a text entry box for 
# typing in colours 
e = tkinter.Entry(root,font= ("Ubuntu", 28)) 

# run the 'startGame' function 
# when the enter key is pressed 
root.bind('<Return>', startGame) 
e.pack()


# set focus on the entry box 
e.focus_set()
# Reset the game:
def restart():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)

def howtoplay():
    root = tkinter.Tk() 
    root.resizable(0,0)
    root.title("Color Game For FreeBSD: How to play:")

    labelTitle = ttk.Label(root,font=("Ubuntu", 26,"bold","underline"),anchor='center', text="How to play this game?")
    label = ttk.Label(root,font=("Ubuntu", 16,"bold",),anchor='center', text="You will need to type down the color of the text. Not what the text says what the color is.")
    label3 = ttk.Label(root,font=("Ubuntu", 16,"bold",),anchor='center',text="You will need to be fast to get more points but needs to be written correctly and the right color.")
    labelw = ttk.Label(root,font=("Ubuntu", 16,"bold",),anchor='center',text="You will lose one point if you make a mistake.")
    label4 = ttk.Label(root,font=("Ubuntu", 16,"bold",),anchor='center',text="Press the enter key to submit you answer.")
    labelTitle.pack(side="top",fill="x",pady=1)
    label.pack(side="top", fill="x", pady=2)
    label3.pack(side="top", fill="x", pady=3)
    labelw.pack(side="top",fill="x",pady=4)
    label4.pack(side="top",fill="x", pady=5)


    B1 = tk.Button(root, text="Exit",font=("ubuntu",28),bg="pink",activebackground='#23d18b', command = root.destroy)
    B1.pack()




Tbutton = tkinter.Button(root,text = "Restart The Game.",font=("ubuntu",28),bg="pink",activebackground='#23d18b', command = restart)
Tbutton.pack(side=tk.LEFT)
Tbutton.place(relx=0.5, rely=0.9, anchor=CENTER)
qbutton = tkinter.Button(root,text = "How to play?",font=("ubuntu",28),bg="pink",activebackground='#23d18b', command = howtoplay)
qbutton.pack(side=tk.LEFT)
qbutton.place(relx=0.5, rely=0.8, anchor=CENTER)
# start the GUI 

root.mainloop() 
