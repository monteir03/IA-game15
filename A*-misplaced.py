from Board import *
from NodeMis import *
import heapq
import time

#algoritmo geral misturado com best-first.search
def best_first_search(start,func): #func é uma variável que recebe um funçao(usamos sempre func)
    visto=set()
    h=[]

    if (not start.possible()):
        print("Impossible To Solve! ")
        return False

    no=NodeMis(start)
    heapq.heappush(h,no)
    visto.add(no_tuplo(no))

    while(len(h)>0):
        prinode=heapq.heappop(h) #este algortimo faz pop sempre do primeiro elemento
        if prinode.NodeSolution():
            x = len(visto)
            print("Memory:", x)
            y = len(prinode.path())-1
            print("Path:", y)
            return prinode.path()#a fazer
        child_list=prinode.expandNode()
        h=func(h,child_list,visto)

    print("Solution Not Found")
    return False

#funçao de inserçao g+h
def insert_gh(heap,child_list,visto):
    for i in child_list:
        if no_tuplo(i) not in visto:
            i.heur+=i.depth
            heapq.heappush(heap,i)
            visto.add(no_tuplo(i))
    return heap

#A star algorithm
def astar(start):
    return best_first_search(start,insert_gh)

#estando a usar nos com heuristica misplaced:
def Amisplaced():
    print("A* - Heuristic Misplaced")
    start=[int(n) for n in input().split()]
    goal=[int(n) for n in input().split()]
    mstart=list_to_matrix(start)
    jogo=Board(mstart,goal)

    inicio=time.time()
    result=astar(jogo)
    fim=time.time()
    total=fim-inicio
    print("Execution Time:", total)

    if result!=False:
        for i in result:
            print(i.brd)
    return 

Amisplaced()

