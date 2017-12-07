import random


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

correct=[]
game=[]
n=0

correct=init_game()
#print(correct)

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
