def merge(array, auxiliar, low, mid, high):
    i = low
    j = mid+1
    k = low
    
    while(i <= mid and j <=high):
        if array[i] < array[j]:
            auxiliar[k] = array[i]
            i+=1
        else:
            auxiliar[k] = array[j]
            j+=1
        k+=1
    # Cuando i o j lleguen a su límite
    while (j <=high):
        auxiliar[k] = array[j]
        j+=1 
        k+=1
    while (i <=mid):
        auxiliar[k] = array[i]
        i+=1
        k+=1
    
    for i in range(low,high+1):
        array[i] = auxiliar[i]


def sort(array, auxiliar,low, high):
    if low < high:
        mid = (low+high)//2
        sort(array, auxiliar, low, mid)
        sort(array, auxiliar, mid+1, high)
        merge(array, auxiliar, low, mid, high)

def mergeSort(array):  
    aux = [0 for i in range(len(array))]    
    sort(array,aux,0,len(array)-1)
    return array
    
def binarySearch(array,point, low, high):
    while (high>=low):
        mid = low+(high-low)//2
        equal = point.compareTo(array[mid])
        if equal == 0:
            return mid
        elif equal == -1:
            high = mid-1
        else:
            low = mid+1
        mid = low+(high-low)//2
    return -1

    

