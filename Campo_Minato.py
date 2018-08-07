import math
import random

class Casella:
    posizione_bombe = []
    caselle_uscite = []

    def __init__(self, x=0, y=0, bombeVicine=0):
        self.x = x
        self.y = y
        self.bombeVicine = bombeVicine

    def ditanza_dalla_casella(self, other):
        return distanza_tra_punti(self, other) <= math.sqrt(2)

    def check_bomba(self):
        return (self.x,self.y) in Casella.posizione_bombe

    def check_casella_uscita(self):
        return (self.x,self.y) in Casella.caselle_uscite

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

# def check_bomba(x,y):
#     global posizione_bombe
#     return (x,y) in posizione_bombe
#
w, h = 8, 5;
bombe = 3
bombe_create = 0

while bombe_create != bombe:
    bomba = Casella()
    bomba.x = random.randint(1,w-1)
    bomba.y = random.randint(1,h-1)
    if not bomba.check_bomba():
        Casella.posizione_bombe.append((bomba.x,bomba.y))
        bombe_create += 1

print(Casella.posizione_bombe)
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
        casella = Casella()
        casella.x = alfabeto.index(scelta[0])
        casella.y = int(scelta[1])
        if casella.check_bomba():
            print("Vabbe ma allora sei un COGLIONE! Hai perso!!!")
            numero_caselle = 0
            break
        elif casella.check_casella_uscita():
            print ("Hai già scelto questa casella, per favore prova di nuovo!")
            break
        else:
            for bomba_prova in range(bombe):
                bomba = Casella()
                bomba.x = Casella.posizione_bombe[bomba_prova][0]
                bomba.y = Casella.posizione_bombe[bomba_prova][1]
                if casella.ditanza_dalla_casella(bomba):
                    casella.bombeVicine += 1
            print(casella.bombeVicine)
            campo[int(casella.y)][casella.x] = casella.bombeVicine
            print_griglia(campo)
    else:
        print("Scegli dei valori corretti")
    if numero_caselle <= bombe:
        print ("Congratulazioni! Hai vinto!!!")
        break
