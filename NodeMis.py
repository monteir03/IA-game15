from Board import *

class NodeMis:

    def __init__(self,brd,parent=None):
        self.brd = brd 
        self.parent = parent
        self.children = [] 
        self.depth=0
        self.heur=self.misplaced() 
      
        if parent:                                     
            self.depth = parent.depth + 1  

    def __eq__(self,other):
        if self.heur==other.heur:
            return True
        return False
    
    def __lt__(self,other):
        if self.heur<other.heur:
            return True
        return False
    
    def get_brd(self):
        return self.brd
    
    def get_parent(self):
        return self.parent 
    
    def path(self):
        path = []
        node = self
        while node is not None:
            path.append(node)
            node = node.get_parent()
        return list(reversed(path))
    
    def NodeSolution(self):
        if not self.brd.isSolution():
            return False
        return True
    
    def expandNode(self):
        #left
        o=self.brd.expand("left")
        if o!=False:
            l=NodeMis(o,parent=self)#no
            self.children.append(l)
        #rigth
        e=self.brd.expand("right")
        if e!=False:
            r=NodeMis(e,parent=self)#no
            self.children.append(r)
        #up
        n=self.brd.expand("up")
        if n!=False:
            u=NodeMis(n,parent=self)#No
            self.children.append(u)
        #down
        s=self.brd.expand("down")
        if s!=False:
            d=NodeMis(s,parent=self)#no
            self.children.append(d)

        return self.children

#heuristicas
    def misplaced(self):
        return self.brd.out_of_place()
    
    def manhattan(self):
        return self.brd.manhattan_distance()

