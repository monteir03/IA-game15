from Board import *
from Node import *
import heapq
import time

#algoritmo geral misturado com best-first.search
def best_first_search(start,func): #func é uma variável que recebe um funçao(usamos sempre func)
    visto=set()
    h=[]

    if (not start.possible()):
        print("Impossible To Solve! ")
        return False

    no=Node(start)
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

#funçao inserçao g
def insert_g(heap,child_list,visto):#gulosa
    for i in child_list:
        if no_tuplo(i) not in visto:
            heapq.heappush(heap,i)
            visto.add(no_tuplo(i))
    return heap

#greedy algorithm
def greedy_search(start):
    return best_first_search(start,insert_g)

#estando a usar nos com heuristica misplaced:
def Greedymanhattan():
    print("Greedy Search - Heuristic Manhattan")
    start=[int(n) for n in input().split()]
    goal=[int(n) for n in input().split()]
    mstart=list_to_matrix(start)
    jogo=Board(mstart,goal)

    inicio=time.time()
    result=greedy_search(jogo)
    fim=time.time()
    total=fim-inicio
    print("Execution Time:", total)

    if result!=False:
        for i in result:
            print(i.brd)
    return 

Greedymanhattan()
