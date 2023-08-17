class Shell:
    
    #insertion sort ~ 1/4N^2 se mueve j hasta encontrar una posicion en la que siga un elemento menor o pos 0
    def InsertionSort(self, array):

        N = len(array)

        for i in range(N):
            
            for j in range(i,0, -1):
                if (self.less(array[j],array[j-1])<0):
                    self.exchange(array, j, j-1)
                else:
                    break
        
        return array
    # Shell sort in python


    # def shellSort(self, array):

    #     # Rearrange elements at each n/2, n/4, n/8, ... intervals
    #     N = len(array)
    #     interval = 1

    #     while (interval<N/3):
    #         interval = 3*interval+1

    #     while interval > 0:
    #         for i in range(interval, N):
    #             j = i
    #             while j >= interval and self.less(array[j],array[j-interval]<0) :
    #                 self.exchange(array, j, j-interval)
    #                 j -= interval

    #         interval //= 2
        
    #     return array

    # ~O^3/2 Acurrated model has not benn descovered
    def ShellSortKnuth(self, array):
    
        N = len(array)
        interval = 1

        while (interval<N/3):
            interval = 3*interval+1

        while interval > 0:
            for i in range(interval, N):
                j = i
                while (j >= interval and self.less(array[j],array[j-interval])) :
                    self.exchange(array, j, j-interval)
                    j -= interval

            interval //= 2
        
        return array
    
    # Determina si es menor(-1) mayor (1) o igual (0)
    def less(self, actual,next)->int:
        # mayor o menor sienndo puntos 2d

        return actual<next

    
    # Se cambian las posiciones
    def exchange(self, list, i, j)->None:

        temp = list[i]
        list[i] = list[j]
        list[j] = temp
