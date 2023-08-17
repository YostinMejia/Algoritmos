from QuickUnion import WeightQuickUnion

class Percolation:
    
    # creates n-by-n grid, with all sites initially blocked
    def __init__(self, n:int) -> None:
        self.grid = []
        self.N = n

        nCuadrado = self.N**2
        self.QU = WeightQuickUnion(nCuadrado+2) #Le sumo 2 porque el valor 0 y n+1 van a ser los nodos virtuales para saber si están conectados
        
        for _ in range(n):
            fila = []
            for _ in range(n):
                fila.append(False)

            self.grid.append(fila)
        
        for i in range(1,n+1):
            self.QU.union(0,i)
            self.QU.union(nCuadrado+1,nCuadrado+1-i)


    # Acceder a una lista con fila(i) y columna(j) como parametros
    def listaIndex(self, i:int, j:int)->int:
        return ((i-1)*self.N)+j

    def Error(self, i:int, j:int)->None:
        if (i<1 or i >self.N or j <1 or j>self.N):
            raise Exception("Fuera del limite")

    #  opens the site (row, col) if it is not open already
    def open(self, row:int, col:int)->None: 
        
        self.Error(row, col)
            
        self.grid[row-1][col-1] = True

        index = self.listaIndex(row,col)

        # Arriba  
        if (row > 1 and self.isOpen(row-1, col)):
            self.QU.union(index, self.listaIndex(row-1, col))          
        # Abajo  
        if (row < self.N and self.isOpen(row+1, col)):
            self.QU.union(index, self.listaIndex(row+1, col))         
        # Izquierda  
        if (col > 1  and self.isOpen(row, col-1)):
            self.QU.union(index, self.listaIndex(row, col-1))         
        # Derecha 
        if (col < self.N and self.isOpen(row, col+1)):
            self.QU.union(index, self.listaIndex(row, col+1)) 
        
    
    # is the site (row, col) open?
    def isOpen(self, row:int, col:int)->bool:
        self.Error(row, col)
        return self.grid[row-1][col-1]

    # is the site (row, col) full?
    # Es decir si está conectado con el top
    def isFull(self, row:int, col:int)->bool:
        self.Error(row, col)
        index = self.listaIndex(row-1, col-1)
        return self.QU.connected(index,0)
        

    #  // returns the number of open sites
    def numberOfOpenSites(self)->int:
        return (self.N**2 - self.QU.count)
    
    # // does the system percolate?
    def percolates(self)->bool:
        # Retornar si la raiz top, está unida con la raiz bottom
        return self.QU.connected(0,self.N**2+1)

    def printGrid(self):
        for i in self.grid:
            print(i)


