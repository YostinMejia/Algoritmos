
def BinarySearch(lista, valor):

    inicio = 0
    final = len(lista)-1
    
    while ( inicio <= final):
        mitad = inicio+(final-inicio)//2

        if (valor < lista[mitad]):
            final=mitad
        elif (valor > lista[mitad]):
            inicio = mitad+1
        else:
            return mitad
    
    return -1


