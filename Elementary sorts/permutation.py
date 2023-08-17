"""Pregunta 2 Permutation. Given two integer arrays of size n, 
design a subquadratic algorithm to determine whether one is a permutation of the other. 
That is, do they contain exactly the same entries but, possibly, in a different order."""

from shellsort import Shell

def Permutation(arr1:list, arr2:list)->bool:

    orden = Shell()
    
    orden.ShellSortKnuth(arr1)# O(N^3/2)
    orden.ShellSortKnuth(arr2)

    N1 = len(arr1)
    N2 = len(arr2)
    if N1 != N2:
        return False

    for i in N1:
        if (arr1[i] != arr2[i]):
            return False
        return True
    
    return True


a =[1,3,5,7,9]

b = [9,7,5,3,1]

print(Permutation(a,b))