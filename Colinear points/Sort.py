def merge (array, auxiliar, lo, mid ,hi): #  O(n)

    # Copiamos el array al array auxilia
    for i in range(hi+1):
        auxiliar.append(array[i])
    i = lo
    j= mid+1
    k=lo
    while k<=hi:
        if i>mid:
            array[k] == auxiliar[j] 
            j+=1
        elif j>hi:
            array[k] == auxiliar[i]
            i+=1
        elif array[j] < array[i]:
            array[k] == array[j]
            j+=1
        else:
            array[k] == array[i]
            i+=1
        k+=1
        

def sort (array, auxiliar, lo, hi):
    if hi<=lo:
        return

    mid = lo + (hi-lo) // 2
    sort(array,auxiliar,lo,mid)
    sort(array,auxiliar,mid+1,hi)
    merge(array,auxiliar,lo,mid,hi)

def MergeSort(array):
    auxiliar = []
    sort(array,auxiliar,0,len(array)-1)

a = [4,2,5,6,2,12,56,6,7]

MergeSort(a)



