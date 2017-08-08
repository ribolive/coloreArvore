elementos = {}
conj = set()
conj.add(3)
conj.add(4)
elementos[1] = conj
conj2 = set()
conj2.add(2)
elementos[2] = conj2

# CONJ = [1, 3]
# CONJ2 = [1]

for i in range(1,6): # TROCAR O 5 POR GRAU MAX
    if not ((i in elementos[1] ) or (i in elementos[2])):
        print(i)
        break