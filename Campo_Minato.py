import math
import random
import copy

class Casella:
    posizione_bombe = []
    caselle_uscite = []
    caselle_vicine = []

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

    def check_esistenza(self):
        return 0 < self.x <= w-1 and 0 < self.y <= h-1

    def check_bombeVicine(self):
        for bomba_prova in range(bombe):
            bomba = Casella()
            bomba.x = Casella.posizione_bombe[bomba_prova][0]
            bomba.y = Casella.posizione_bombe[bomba_prova][1]
            if self.ditanza_dalla_casella(bomba):
                self.bombeVicine += 1
        campo[int(self.y)][self.x] = self.bombeVicine

    # def trova_vicini(self):
    #     for m in range(1,w):
    #         for n in range(1,h):
    #             if math.sqrt((self.x - m) ** 2 + (self.y - n) ** 2) <= math.sqrt(2) and math.sqrt((self.x - m) ** 2 + (self.y - n) ** 2) != 0:
    #                 Casella.caselle_vicine.append((m, n))

    def caselle_diagonali(self):
        if self.bombeVicine == 0:
            for n in range(-1, 2, 1):
                for m in range(-1, 2, 1):
                    if (m**2 + n**2)==2:
                        casella_vuota = copy.copy(casella)
                        casella_vuota.x += n
                        casella_vuota.y += m
                        Casella.caselle_vicine.append(casella_vuota)
                    else:
                        casella_vuota = copy.deepcopy(casella)
                        casella_vuota.caselle_vuote_vicine(m,n)

    def caselle_vuote_vicine(self,m,n):
        while self.bombeVicine == 0 and (3 * m + 2 * n) != 0:
            self.x += n
            self.y += m
            if self.check_esistenza():
                self.check_bombeVicine()
            else:
                break

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
            casella.check_bombeVicine()
            casella.caselle_diagonali()

            for caselle_diagonali in Casella.caselle_vicine:
                print (caselle_diagonali)
                if caselle_diagonali.check_esistenza():
                    if caselle_diagonali.check_bombeVicine()==0:
                        caselle_diagonali.caselle_diagonali()



            # if casella.bombeVicine == 0:
            #     for n in range(-1, 2, 1):
            #         for m in range (-1, 2, 1):
            #             if m+n == 0 or abs(m)+abs(n)==2:
            #                 continue
            #             else:
            #                 casella_vuota = copy.deepcopy(casella)
            #                 casella_vuota.caselle_vuote_vicine()

                        # while casella_vuota.bombeVicine == 0 and (3*m + 2*n)!=0:
                        #     casella_vuota.x += n
                        #     casella_vuota.y += m
                        #     if casella_vuota.check_esistenza():
                        #         casella_vuota.check_bombeVicine()
                        #     else:
                        #         break

            # if casella.bombeVicine == 0:
            #     casella.trova_vicini()
            #     for i in Casella.caselle_vicine:
            #         casella_vuota = Casella()
            #         casella_vuota.x = i[0]
            #         casella_vuota.y = i[1]
            #         for bomba_prova in range(bombe):
            #             bomba = Casella()
            #             bomba.x = Casella.posizione_bombe[bomba_prova][0]
            #             bomba.y = Casella.posizione_bombe[bomba_prova][1]
            #             if casella.ditanza_dalla_casella(bomba):
            #                 casella.bombeVicine += 1
            #             campo[casella_vuota.y][casella_vuota.x] = casella_vuota.bombeVicine


            print_griglia(campo)
    else:
        print("Scegli dei valori corretti")
    if numero_caselle <= bombe:
        print ("Congratulazioni! Hai vinto!!!")
        break
