
w, h = 8, 5;
campo = [[0 for x in range(w)] for y in range(h)]

alfabeto = ("A", "B", "C", "D", "E")

campo [0] = alfabeto

#for m in range(len(alfabeto)):
#    campo [m] = alfabeto [m]


print(campo)
print(' '+'\n'.join([''.join(['{:}'.format(item) for item in row])
      for row in campo]))