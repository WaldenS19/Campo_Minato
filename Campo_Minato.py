import random
import math

class Casella:
    caselle_uscite = []
    posizione_bombe = []

    def __init__(self, x=0, y=0, bombeVicine=0):
        self.x = x
        self.y = y
        self.bombeVicine = bombeVicine

    #Caselle già uscite
    def casella_selezionata(self):
        Casella.caselle_uscite.append((self.x, self.y))

    def check_casella_uscita(self):
        return (self.x, self.y) in Casella.caselle_uscite

    #Check se ho colpito la bomba
    def check_bomba(self):
        return (self.x, self.y) in Casella.posizione_bombe

    #La casella è limitrofa?
    def caselle_vicine(self,other):
        return 0 < math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2) <= math.sqrt(2)

    #Numero di bombe vicine
    def check_bombeVicine(self):
        for bomba_prova in range(bombe):
            bomba = Casella()
            bomba.x = Casella.posizione_bombe[bomba_prova][0]
            bomba.y = Casella.posizione_bombe[bomba_prova][1]
            if self.caselle_vicine(bomba):
                self.bombeVicine += 1
        campo[int(self.y)][self.x] = self.bombeVicine
        self.casella_selezionata()

    #Ciclo su tutta la griglia per quanto riguarda gli zzei
    def ciclo_zeri(self):
        for m in range(1, ymax):
            for n in range(1, xmax):
                casella_vuota = crea_casella(n, m)
                if casella_vuota.caselle_vicine(self) and not casella_vuota.check_casella_uscita():
                    casella_vuota.check_bombeVicine()
                    if casella_vuota.bombeVicine == 0:
                        casella_vuota.ciclo_zeri()


# Creazione griglia
xmax, ymax= input ("Inserisci le dimensioni del campo con cui vuoi giocare (dimensioni massime 19*19) --> ").split()
xmax, ymax = int(xmax), int(ymax);
numero_caselle = (xmax-1)*(ymax-1)
fineGioco = False
campo = [["?" for x in range(xmax)] for y in range(ymax)]
alfabeto = (" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S")
campo [0] = alfabeto[:xmax]
for i in range(ymax-1):
    campo[i+1][0]=i+1
def printgriglia(griglia):
    print('\n'.join([' '.join(['{}'.format(item) for item in row])
          for row in campo]))
printgriglia(campo)

# Funzione creazione classe (per non ripeterla 10k volta
def crea_casella(x, y):
    casella = Casella()
    casella.x = x
    casella.y = y
    return casella

#Conta caselle ancora da apire: in input gli passo il campo da gioco
def caselle_rimanenti(griglia):
    global numero_caselle
    numero_caselle = 0
    for numeri in griglia:
       for numero in numeri:
           if numero == "?":
               numero_caselle += 1
    return(numero_caselle)

# Crazione bombe
dati_corretti = False
while dati_corretti == False:
    bombe = input('Inserisci il numero delle bombe con cui vuoi giocare --> ')
    bombe = int(bombe)
    if bombe < xmax*ymax:
        dati_corretti = True

bombe_create = 0
def creazione_bombe():
    global bombe_create
    while bombe_create != bombe:
        bomba = Casella()
        bomba.x = random.randint(1,xmax-1)
        bomba.y = random.randint(1,ymax-1)
        if ((bomba.x, bomba.y) not in Casella.posizione_bombe) and ((bomba.x, bomba.y) not in Casella.caselle_uscite):
            Casella.posizione_bombe.append((bomba.x, bomba.y))
            bombe_create += 1

#Dopo la prima scelta
def primogiro():
    global numero_caselle
    numero_caselle -= 1
    casella = crea_casella(alfabeto.index(scelta[0]), int(scelta[1]))
    creazione_bombe()
    casella.check_bombeVicine()
    if casella.bombeVicine == 0:
        casella.ciclo_zeri()
    printgriglia(campo)

#Inizio gioco
while numero_caselle > bombe and fineGioco == False:
    scelta = input('Inserisci le coordinate della casella --> ')
    if (scelta[0] not in alfabeto[1:xmax]) or (int(scelta[1]) not in range(ymax)):
        print("Scegli dei valori corretti")
    elif numero_caselle == (xmax-1)*(ymax-1):
        primogiro()
    else:
        casella = crea_casella(alfabeto.index(scelta[0]), int(scelta[1]))
        if casella.check_casella_uscita():
            print ("Hai già scelto questa casella, per favore prova di nuovo!")
        elif casella.check_bomba():
            print("Vabbe ma allora sei un COGLIONE! Hai perso!!!")
            fineGioco = True
        elif (scelta[0] in alfabeto[1:xmax]) and (int(scelta[1]) in range(ymax)):
            casella.check_bombeVicine()
            if casella.bombeVicine == 0:
                casella.ciclo_zeri()
            printgriglia(campo)
        else:
            print("Scegli dei valori corretti")
    numero_caselle = caselle_rimanenti(campo)
    if numero_caselle <= bombe:
        print ("Congratulazioni! Hai vinto")

