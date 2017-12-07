import random
import tkinter as tk
from functools import partial

fact = 1.6
bfact = 2

def init_game():
    """
    	Commande appelée par __MAIN
        Réinitialise le jeu : variables de cooerdonnées, variable de saisie des couleurs et combinaison correcte
        Génere une nouvelle combinaison correcte parmis les 8 couleur possibles sans doublon
        Renvoie la combinaison correcte (correct).
    """ 
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
    """
        Commande appelée par init_game()
        (Ré)initialise le canvas
        Crée une grille de 4x10 carrés gris sur fond blanc(30x30px)
        Crée une ligne noire 5px sous le dernier carré
        Ne renvoie rien.
    """
    global canvas
    canvas = tk.Canvas(app, width=300*fact, height=400*fact, bg ='white')
    canvas.grid(row=1, column=0, columnspan=8)
    for i in range(10):
        for j in range(4):
            canvas.create_rectangle(10*fact + 35*fact*j, 10*fact + 35*fact*i, (10*fact + 35*fact*j) + 30*fact, (10*fact + 35*fact*i) + 30*fact, fill='grey')
    canvas.create_line(0, 360*fact, 300*fact, 360*fact)

            
def check_play(gm):
    """
        Commande appelée par send_game()
        Initialise la séquence de test de comparaison Combinaison prposée vs Combinaison correcte (game==correct ?)
        Vérifie si le jeu est gagné ou perdu
        Si c'est le cas ; appelle game_test(gm) ; affiche la combinaison correcte et un message "GAME OVER"
        Sinon ; appelle game_test(gm)
        Ne renvoie rien.
    """
    global coordY
 
    if gm == correct or coordY > 8:
        game_test(gm)
        for i, color in enumerate(correct):
            canvas.create_rectangle(10*fact + 35*fact*i, 365*fact, (10*fact + 35*fact*i) + 30*fact, 395*fact, fill=color)
        coordY += 13*fact
        canvas.create_text(225*fact, 380*fact, font="Arial 22 bold", text="GAME OVER")
     
    else:
        game_test(gm)


def game_test(gm):
    """
        Commande appelée par check_play()
        Effectue le test de comparaison Combinaison prposée vs Combinaison correcte
        Parcourt la liste game en comparant les éléments un à un avec correct
        Si les deux éléments concordent ; affiche un rond noir à côté de la ligne (coordonné X (coordX) corespondante)
        Sinon si l'élement est dans la liste ; affiche un rond blanc à côté de la ligne (coordonné X (coordX) corespondante)
        Ne renvoie rien.
    """
    black = 0
    white = 0
    for i in range(len(gm)):
        if gm[i] == correct[i]:
            black += 1
        elif gm[i] in correct:
            white += 1
    for i in range(black):
         canvas.create_oval(160*fact + 13*fact*i, 14*fact + 35*fact*coordY, 170*fact + 13*fact*i, (14*fact + 35*fact*coordY) + 10*fact, fill="black")
    for i in range(white):
         canvas.create_oval(160*fact + 13*fact*i, 27*fact + 35*fact*coordY, 170*fact + 13*fact*i, (27*fact + 35*fact*coordY) + 10*fact, fill="white")


def click_bt(cl,event):
    """
        Commande appelée par le bind() d'un bouton de couleur (b)
        Prend  la couleur du bouton comme argument
        Affiche un carré de 30x30px  à l'emplacement correspondant aux coordonnées courrantes (coordX et coordY)
        Vérifie que la coordonnée X est possible
        Dans le cas contraire (valeur hors de la grille) ; réinitialiste la coordonnée
        Ne renvoie rien.
    """
    global coordX
    global coordY
    global game

    if coordX > 3:
        coordX = 0
        game = []
    canvas.create_rectangle(10*fact + 35*fact*coordX, 10*fact + 35*fact*coordY, (10*fact + 35*fact * coordX) + 30*fact, (10*fact + 35*fact*coordY) + 30*fact, fill=cl)
    coordX += 1
    game.append(cl)


def send_game():
    """
        Commande appelée par le bouton "SEND"
        Verifie que la Combinaison proposée (game) a bien 4 couleurs et 4 couleurs différentes
        Si c'est le cas ; appelle check_play() ;
        réinitialise la variable Combinaison proposée (game) ;
        réinitialise la variable de coordonnée X (coordX) ;
        incrémente la variable de coordonnée Y (coordY)
        Sinon ; appelle reset_row()
        Ne renvoie rien.
    """
    global coordX
    global coordY
    global game

    if (len(game) < 4) or (game[0] in game[1:]) or (game[1] in game[2:]) or (game[2]==game[3]):
        reset_row()
    else:
        check_play(game)
        game = []
        coordX = 0
        coordY += 1


def reset_row():
    """
    	Commande appelée par le bouton "RESET"
    	Affiche 4 carrés gris sur la grille, à la coordonnée Y
    	Reinitialise la valeur de la liste Combinaison proposée (game)
    	Réinitialise la coordonée X (coordX)
    	Ne renvoie rien.
    """
    global game
    global coordX

    for j in range(4):
        canvas.create_rectangle(10*fact + 35*fact*j, 10*fact + 35*fact*coordY, (10*fact + 35*fact*j) + 30*fact, (10*fact + 35*fact*coordY) + 30*fact, fill='grey')
    coordX = 0
    game = []


tkcolors = ["DeepPink2", "lavender", "red3", "DeepSkyBlue4", "green3", "yellow2", "purple3", "orange3"]

app = tk.Tk()

app.title("____MASTERMIND____")

new_game = tk.Button(app, text='NEW GAME', command=init_game, width=int(10*bfact), height=int(bfact))             #Crée un bouton "NEW GAME" qui appelle init_game()
new_game.grid(row=0, column=0, columnspan=8, sticky=tk.N)

for i, color in enumerate(tkcolors):                                                #Crée 8 boutons de couleurs différentes
                                                                                    # (présentes dans la liste tkcolors)
    b = tk.Button(app, text='', height=int(bfact), width=int(1.5*bfact), bg=color, activebackground=color)      #Pour Windaube
#    b = tk.Button(app, text='', width=1, bg=color, activebackground=color)     #Pour Nunux
    b.grid(row=20, column=i)
    b.bind("<Button-1>",partial(click_bt,color))                                    # qui appelent respectivement click_bt(leur couleur)

send = tk.Button(app, text='SEND', command=send_game, width=int(10*bfact), height=int(bfact))                   # Crée un bouton "SEND" qu appelle send_game()
send.grid(row=40, column=0, columnspan=3, sticky=tk.E)
reset = tk.Button(app, text='RESET', command=reset_row, width=int(10*bfact), height=int(bfact))                  #Crée un bouton "RESET" qui appele reset_row()
reset.grid(row=40, column=4, columnspan=3, sticky=tk.E)

init_game()                                                                         #Initialise une nouvelle partie (cf. docstring)

app.mainloop()
