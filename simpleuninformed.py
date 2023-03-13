#Este ficheiro apresenta todas as funçoes necessarias para estratégias nao informadas, não iterativas e não limitadas! 
#DFS BFS
from Board import *
from Node import *
from collections import deque
                                     
def general_search_algorithm(start,func):
    visto=set()
    dq=deque()

    if (not start.possible()):
        return -1  #impossivel de resolver
    
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
        dq=func(dq,child_list,visto)

    return 0 #sem soluçao

#queueing func
def insert_bfs(deque,child_list,visto):
    for i in child_list:
        if no_tuplo(i) not in visto:
            deque.append(i)
        visto.add(no_tuplo(i))
    return deque

def insert_dfs(deque,child_list,visto):
    for i in child_list:
        if no_tuplo(i) not in visto:
            deque.appendleft(i)
        visto.add(no_tuplo(i))
    return deque

# dfs & bfs final
def deepth_first_search(start):
    return general_search_algorithm(start,insert_dfs)

def breath_first_search(start):
    return general_search_algorithm(start,insert_bfs)
