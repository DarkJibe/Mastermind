import random
import tkinter as tk

def init_game():
#    i=0
#    while i<4:
#        x=random.randint(1,8)
#        while x in correct:
#            x=random.randint(1,8)
#        correct.append(x)
#        i+=1
    liste=["1","2","3","4","5","6","7","8"]
    return random.sample(liste,4)

def check_play():
    black=0
    white=0
    if game==correct:
        return True
    else:
        for i in range(len(game)):
            if game[i]==correct[i]:
                black+=1
            elif game[i] in correct:
                white+=1
        print(game,"=> Black =",black,"White =",white)
        return False

def click_bt(event):
    for i in range():
        canvas.create_rectangle()
    return -1

def send():
    return -1

def reset_row():
    return -1


correct=[]
game=[]
n=0

correct=init_game()
#print(correct)


tkcolors = ["white", "black", "red", "blue", "green", "yellow", "purple",
            "orange"]

app = tk.Tk()

app.title("____Mastermind____")

new_game = tk.Button(app, text='NEW GAME', command=init_game, width=10)
new_game.grid(row=0, column=0, columnspan=8, sticky=tk.W)

canvas = tk.Canvas(app, width=300, height=450, bg ='white')
canvas.grid(row=1, column=0, columnspan=8)

for i in range(10):
    for j in range(4):
        canvas.create_rectangle(10+35*j,10+35*i,(10+35*j)+30,(10+35*i)+30,fill='grey')
        

for i, color in enumerate(tkcolors):
    b = tk.Button(app, text='', width=1, bg=color, activebackground=color)
    b.grid(row=20, column=i)
    b.bind("<Button-1>",click_bt)

send = tk.Button(app, text='SEND', command=send, width=10)
send.grid(row=40, column=0, columnspan=3, sticky=tk.E)
reset = tk.Button(app, text='RESET', command=reset_row, width=10)
reset.grid(row=40, column=4, columnspan=3, sticky=tk.E)

#init_game()

app.mainloop()

"""
while True:
    n+=1
    game=input("Jouez 4 couleurs parmis [1,8] séparées d'un espace :")
    game=list(game)
    for i in game:
        if i==' ':
            z=game.index(i)
            del game[z]
    if check_play():
        print("Vous avez gagné en",n,"coups !")
        break

print("Fait.")
"""
