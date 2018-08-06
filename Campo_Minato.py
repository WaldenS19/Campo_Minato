import math
import random

class Casella:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def ditanza_dalla_casella(self, other):
        return distanza_tra_punti(self.casella, other) <= math.sqrt(2)


class Bomba(Casella):
    def __init__(self, x, y, bomba=True):
        super().__init__(x, y)
        self.bomba = bomba

class Vuota(Casella):
    def __init__(self, x, y, bombeVicine=9):
        super().__init__(x, y)
        self.bombeVicine = bombeVicine

def distanza_tra_punti(p1, p2):
    """Calcola la distanza tra due oggetti Caselle"""
    return math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)

def print_griglia(griglia):
    print('\n'.join([' '.join(['{}'.format(item) for item in row])
                     for row in griglia]))

def caselle_rimanenti(griglia):
    global numero_caselle
    numero_caselle = 0
    for numeri in griglia:
        for numero in numeri:
            if numero == "?":
                numero_caselle += 1
    return(numero_caselle)

def check_bomba(x,y):
    global posizione_bombe
    return (x,y) in posizione_bombe

w, h = 8, 5;
bombe = 3
for b in range(bombe):
    
posizione_bombe = (2,3), (3,4), (3,5)

numero_caselle=w*h
campo = [["?" for x in range(w)] for y in range(h)]
alfabeto = (" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "L")
campo [0] =  alfabeto[:w]

for i in range(h-1):
    campo[i+1][0] = i+1

print_griglia(campo)

while True:
    scelta = input('Inserisci le coordinate della casella --> ')
    if (scelta[0] in alfabeto[:w]) and (int(scelta[1]) in range(h)):
        break
    else:
        print("Scegli dei valori corretti")
    if numero_caselle <= bombe:
        print ("Congratulazioni! Hai vinto!!!")
        break
