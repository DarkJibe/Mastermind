import random
import tkinter as tk
from functools import partial

def init_game():
    
    global correct
    global coordX
    global coordY
    global game

    coordY=0
    coordX=0
    game=[]
    
    grille()
    liste=["DeepPink2", "lavender", "red3", "DeepSkyBlue4", "green3", "yellow2", "purple3",
            "orange3"]
    correct=random.sample(liste,4)
    return correct

def grille():
    global canvas
    canvas = tk.Canvas(app, width=300, height=400, bg ='white')
    canvas.grid(row=1, column=0, columnspan=8)
    for i in range(10):
        for j in range(4):
            canvas.create_rectangle(10+35*j,10+35*i,(10+35*j)+30,(10+35*i)+30,fill='grey')
    canvas.create_line(0, 360, 300, 360)   
    

def check_play(gm):
    black=0
    white=0
    if gm==correct or coordY>8:
        for i,color in enumerate(correct):
            canvas.create_rectangle(10+35*i,365,(10+35*i)+30,395,fill=color)
        b.unbind("<Button-1>")
        canvas.create_text(225,380,font="Arial 16 bold",text="GAME OVER")
    else:
        for i in range(len(gm)):
            if gm[i]==correct[i]:
                black+=1
            elif gm[i] in correct:
                white+=1
        for i in range(black):
            canvas.create_oval(160+10*i,15+35*coordY,170+10*i,(15+35*coordY)+10,fill="black")
        for i in range(white):
            canvas.create_oval(160+10*i,25+35*coordY,170+10*i,(25+35*coordY)+10, fill="white")

def click_bt(cl,event):
    
    global coordX
    global coordY
    global game

    if coordX>3:
        coordX=0
        game=[]
    canvas.create_rectangle(10+35*coordX,10+35*coordY,(10+35*coordX)+30,(10+35*coordY)+30,fill=cl)
    coordX+=1
    game.append(cl)


def send():
    
    global coordX
    global coordY
    global game

    print(game)
    print(correct)
    check_play(game)
    game=[]
    coordX=0
    coordY+=1


def reset_row():
    
    global game
    global coordX

    for j in range(4):
        canvas.create_rectangle(10+35*j,10+35*coordY,(10+35*j)+30,(10+35*coordY)+30,fill='grey')
    coordX=0
    game=[]


tkcolors =["DeepPink2", "lavender", "red3", "DeepSkyBlue4", "green3", "yellow2", "purple3",
            "orange3"]

app = tk.Tk()

app.title("____MASTERMIND____")

new_game = tk.Button(app, text='NEW GAME', command=init_game, width=10)
new_game.grid(row=0, column=0, columnspan=8, sticky=tk.N)

grille()       

for i, color in enumerate(tkcolors):
    b = tk.Button(app, text='', width=3, bg=color, activebackground=color)     #Pour Windaube
#    b = tk.Button(app, text='', width=1, bg=color, activebackground=color)      #Pour Nunux
    b.grid(row=20, column=i)
    b.bind("<Button-1>",partial(click_bt,color))

send = tk.Button(app, text='SEND', command=send, width=10)
send.grid(row=40, column=0, columnspan=3, sticky=tk.E)
reset = tk.Button(app, text='RESET', command=reset_row, width=10)
reset.grid(row=40, column=4, columnspan=3, sticky=tk.E)

init_game()

app.mainloop()
