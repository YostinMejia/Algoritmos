# https://stackoverflow.com/questions/41340528/dutch-national-flag-deducing-solution

class Pebble:
    def __init__(self, color) -> None:
        self.color = color
    
    def __repr__(self) -> str:
        return f"{self.color}"
        

class Operation:

    def color(self, objeto)->int:
        return objeto.color

    def swap(self, lista, i, j)->None:
        temp = lista[i]
        lista[i] = lista[j]
        lista[j] = temp
    
    def sort(self, array):
        
        N = len(array)
        low = 0
        mid = 0
        high = N-1

        while mid <=high:
            # Derecha del high están los valores mayores
            # Mid pointer apunta al primer valor desconocido
            # A la izquierda del low pointer están los valores menores
            
            # Encuentra un azul
            if self.color(array[mid]) == 0 :
                self.swap(array, mid, low)
                mid+=1
                low+=1
            # Si se encuentra una blanca
            elif self.color(array[mid]) == 1:
                mid+=1
            # Encuentra una roja
            elif self.color(array[mid]) == 2:
                self.swap(array, mid, high)
                high-=1



#arr = [1,2,1,1,0,2,0,1,2,0,0,1,1]
arr = []

for i in range(20):
    for j in range(3):
        arr.append(Pebble(j))

print(arr)
orden = Operation()

orden.sort(arr)

print(arr)

