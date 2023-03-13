#IDFS
from Board import *
from Node import *
from collections import deque
import time

def general_search_algorithm(start,func,max_depth): #func: é uma variável função
    visto=set()
    dq=deque()
    if (not start.possible()):
        return -1

    no=Node(start)
    dq.append(no)
    visto.add(no_tuplo(no))

    while(len(dq)>0):
        fnode=dq.popleft() 
        if fnode.NodeSolution():
            x = len(visto)
            print("Memory:", x)
            y = len(fnode.path())-1
            print("Path:", y)
            return fnode.path()
        child_list=fnode.expandNode()
        dq=func(dq,child_list,max_depth,visto)
    return 0

#queueing func
def insert_dfs_limited(deque,child_list,max_depth,visto):
    for i in child_list:
        if i.depth<=max_depth and  no_tuplo(i) not in visto:
            deque.appendleft(i)
            visto.add(no_tuplo(i))
    return deque
    
#idfs
def iterative_deepening_first_search(start):
    memory=0
    k=0
    while True:
        a=general_search_algorithm(start,insert_dfs_limited,k) #rever memoria deste
        #memory+=()
        k+=1
        if a==-1:
            return False
        if a!=0:
            return a
  
#callable function
def idfs():
    print("IDFS")
    start=[int(n) for n in input().split()]
    goal=[int(n) for n in input().split()]
    mstart=list_to_matrix(start)
    jogo=Board(mstart,goal)

    inicio=time.time()
    res=iterative_deepening_first_search(jogo)
    fim=time.time()
    total = fim-inicio
    print("Execution Time:",total)


    if res==False:
        print("Impossible to solve!")
    else:
        for i in res:
            print(i.brd)

idfs()