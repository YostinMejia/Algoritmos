def Merge(array, auxiliar, low, mid, high):
    i = low
    j = mid+1
    k = low
    
    while(i <= mid and j <=high):
        if array[i] <= array[j]:
            auxiliar[k] = array[i]
            i+=1
        else:
            auxiliar[k] = array[j]
            j+=1
        k+=1
    # Cuando i o j lleguen a su límite
    if (i>mid):
        while (j <=high):
            auxiliar[k] = array[j]
            j+=1 
            k+=1
    else:
        while (i <=mid):
            auxiliar[k] = array[i]
            i+=1
            k+=1
    # 
    

def MergeSort(array, auxiliar,low, high):
    if low < high:
        mid = (low+high)//2
        MergeSort(array, auxiliar, low, mid)
        MergeSort(array, auxiliar, mid+1, high)
        Merge(array, auxiliar, low, mid, high)
    
    
a = [3,4,5,6,1,3]    
aux = [3,4,5,6,1,3]    
# print(aux)
MergeSort(a,aux,0,len(a)-1)
print(aux)


