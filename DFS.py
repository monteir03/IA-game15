from simpleuninformed import *
import time

def dfs():
    start=[int(n) for n in input().split()]
    goal=[int(n) for n in input().split()]
    mstart=list_to_matrix(start)
    jogo=Board(mstart,goal)

    inicio=time.time()
    result=deepth_first_search(jogo)
    fim=time.time()
    total=fim-inicio
    print("Execution Time:", total)

    if result==-1:
        print("Impossible To Solve")
    elif result==0:
        print("Solution Not found ")
    else:
        for i in result:
            print(i.brd)
    return 

dfs()
