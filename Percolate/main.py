from Percolation import Percolation
import random
n = 4
m = Percolation(n)
print(m.printGrid())

# Posiciones disponibles
numeros =[]
for i in range(1,n+1):
    for j in range(1,n+1):
        numeros.append([i,j])

print(numeros)

while not m.percolates():
    
    indice = round(random.randint(0,len(numeros)-1))
    i = numeros[indice][0]
    j = numeros[indice][1]

    m.open(i,j)
    m.printGrid()
    print(m.percolates())