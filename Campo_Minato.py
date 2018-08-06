class casella:

    def __init__(self, posizione):
        self.posizione = posizione

primo_punto = casella(13)

w, h = 8, 5;
campo = [[0 for x in range(w)] for y in range(h)]

alfabeto = ("A", "B", "C", "D", "E")

campo [0] = alfabeto
campo [1] = (1, primo_punto.posizione, "?", "?", "?")

#for m in range(len(alfabeto)):
#    campo [m] = alfabeto [m]



print(' '+'\n'.join([''.join(['{:4}'.format(item) for item in row])
      for row in campo]))