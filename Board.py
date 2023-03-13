from copy import deepcopy

ROWS = 4
COLS = 4

def no_tuplo(n):                          
    m=n.brd.board
    l=correspond_list(m)
    t=tuple(l)
    return t
    
def list_to_matrix(list):
    matrix=[[0 for l in range(4)] for l in range(4)]
    k=0
    for i in range(4):
        for j in range(4):
            matrix[i][j]=list[k]
            k+=1
    return matrix

def inversions(lista):
    inv = 0
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if ((lista[i]>lista[j]) and (lista[i])!=0 and (lista[j])!=0):
                inv += 1
    return inv

def correspond_list(matriz):
    lista = [item for sublist in matriz for item in sublist]
    return lista


#board
class Board:
   
    def __init__(self,matrix,goal):
        self.goal=goal
        self.board=deepcopy(matrix)
        self.blank = self.find_blank()#[x,y]

    def __repr__(self): 
        k=0
        for i in self.board:
            print()
            print("+----+----+----+----+")
            for j in i:
                print("| {:2d} ".format(j), end="")
            print("|", end="")
            if(k<3):
                k += 1
        print()
        print("+----+----+----+----+")
        return "" 
    
    
    def find_blank(self):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col] == 0:
                    return [row, col]

    def isSolution(self):
        if (correspond_list(self.board)==self.goal):
            return True
        return False

    def possible(self):
        lista=correspond_list(self.board)    
        ninv=inversions(lista)              
        iblank=self.blank[0]                     
        if ((ninv%2)!=(iblank%2)):
            return True
        return False

#comandos:
    def up(self):
        if (self.blank[0]>0 and self.blank[0]<=3):
            upper=self.board[self.blank[0]-1][self.blank[1]] 
            self.board[self.blank[0]-1][self.blank[1]]=0
            self.board[self.blank[0]][self.blank[1]]=upper 
            self.blank[0]-=1 
            return True
        return False

    def down(self):
        if (self.blank[0]<3 and self.blank[0]>=0):
            lower=self.board[self.blank[0]+1][self.blank[1]] 
            self.board[self.blank[0]+1][self.blank[1]]=0
            self.board[self.blank[0]][self.blank[1]]=lower
            self.blank[0]+=1 
            return True
        return False
    
    def right(self):
        if (self.blank[1]<3 and self.blank[1]>=0):
            thenext=self.board[self.blank[0]][self.blank[1]+1] 
            self.board[self.blank[0]][self.blank[1]+1]=0
            self.board[self.blank[0]][self.blank[1]]=thenext 
            self.blank[1]+=1 
            return True        
        return False
    
    def left(self):
        if (self.blank[1]>0 and self.blank[1]<=3):
            theprev=self.board[self.blank[0]][self.blank[1]-1] 
            self.board[self.blank[0]][self.blank[1]-1]=0
            self.board[self.blank[0]][self.blank[1]]=theprev
            self.blank[1]-=1 
            return True
        return False
    
    def expand(self,str):
        jogo = deepcopy(self)
        
        if str=="left":
            val=jogo.left()
            if val==False:
                 return False

        elif str=="right":
            val=jogo.right()
            if val==False:
                 return False

        elif str=="up":
            val=jogo.up()
            if val==False:
                 return False

        elif str=="down":
            val=jogo.down()
            if val==False:
                 return False

        return jogo

#heuristicas
    def out_of_place(self):
        soma = 0
        lista = correspond_list(self.board)
        for i in range(len(lista)):
            if lista[i]!=self.goal[i] and lista[i]!=0:
                soma += 1
        return soma
    
    def manhattan_distance(self):
        distancia = 0
        final = list_to_matrix(self.goal)
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j]!=0 and self.board[i][j] != final[i][j]:
                    for k in range(len(final)):
                        if self.board[i][j] in final[k]:
                            distancia += abs(k - i) + abs(final[k].index(self.board[i][j]) - j)
        return distancia

    
        