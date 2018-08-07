import math
import random

class Casella:
    posizione_bombe = []
    caselle_uscite = []

    def __init__(self, x=0, y=0, bombeVicine=0):
        self.x = x
        self.y = y
        self.bombeVicine = bombeVicine

    def conta_caselle(self):
        if self.distanza_dalla_casella(bomba):
            self.bombeVicine += 1

    def distanza_dalla_casella(self, other):
        return distanza_tra_punti(self, other) <= math.sqrt(2)

    def check_bomba(self):
        return (self.x,self.y) in Casella.posizione_bombe

    def check_casella_uscita(self):
        return (self.x,self.y) in Casella.caselle_uscite

    # def check_caselle_limitrofe(self, n, m):
    #     conta = 0
    #     conta = 0
    #     while self.bombeVicine == 0 and self.x < h-1 and self.y < w-1:
    #         self.x += n
    #         self.y += m
    #         for bomba_prova in range(bombe):
    #             Casella.conta_caselle(self)
    #             print(self.bombeVicine)
    #             campo[int(self.y)][self.x] = self.bombeVicine
    #         conta += 1
    #     return conta

    def check_alto(self):
        casella_alto = Casella()
        casella_alto.x = self.x
        casella_alto.y = self.y - 1
        if not casella_alto.check_casella_uscita():
            casella_alto.conta_caselle()
            campo[int(casella_alto.y)][casella_alto.x] = casella_alto.bombeVicine
            if casella_alto.bombeVicine == 0 and casella_alto.y > 1:
                casella_alto.check_alto()

    def check_basso(self):
        casella_basso = Casella()
        casella_basso.x = self.x
        casella_basso.y = self.y + 1
        if not casella_basso.check_casella_uscita():
            casella_basso.conta_caselle()
            campo[int(casella_basso.y)][casella_basso.x] = casella_basso.bombeVicine
            if casella_basso.bombeVicine == 0 and casella_basso.y < h-1:
                casella_basso.check_basso()

    def check_dx(self):
        casella_dx = Casella()
        casella_dx.x = self.x + 1
        casella_dx.y = self.y
        if not casella_dx.check_casella_uscita():
            casella_dx.conta_caselle()
            campo[int(casella_dx.y)][casella_dx.x] = casella_dx.bombeVicine
            if casella_dx.bombeVicine == 0 and casella_dx.x < w-1:
                casella_dx.check_dx()

    def check_sx(self):
        casella_sx = Casella()
        casella_sx.x = self.x - 1
        casella_sx.y = self.y
        if not casella_sx.check_casella_uscita():
            casella_sx.conta_caselle()
            campo[int(casella_sx.y)][casella_sx.x] = casella_sx.bombeVicine
            if casella_sx.bombeVicine == 0 and casella_sx.x > 1:
                casella_sx.check_sx()

    def caselle_zero(self):
        if self.y > 1: self.check_alto()
        if self.y < h - 1: self.check_basso()
        if self.x > 1: self.check_sx()
        if self.x < w - 1: self.check_dx()

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
                casella.conta_caselle()

            print(casella.bombeVicine)
            campo[int(casella.y)][casella.x] = casella.bombeVicine

            while casella.bombeVicine == 0:
                # spostamento_x = Casella.check_caselle_limitrofe(casella, 1, 0)
                # casella.x -= spostamento_x
                # print(casella.x)
                # spostamento_y = Casella.check_caselle_limitrofe(casella, 0, 1)
                # casella.y -= spostamento_y + 1
                casella.caselle_zero()
                break
            print_griglia(campo)
    else:
        print("Scegli dei valori corretti")
    if numero_caselle <= bombe:
        print ("Congratulazioni! Hai vinto!!!")
        break

