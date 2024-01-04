class Graph:
    def __init__(self,heuristic,graph,start_n):
        self.H=heuristic
        self.graph=graph
        self.start=start_n
        self.status={}
        self.parent={}
        self.solution={}
    
    def get_neighbors(self,v):
        return self.graph.get(v,"")
    def get_status(self,v):
        return self.status.get(v,0)
    def set_status(self,v,val):
        self.status[v]=val
    def get_heuristic(self,v):
        return self.H.get(v,0)
    def set_heuristic(self,v,val):
        self.H[v]=val

    def printSolution(self):
        print("Traversing from Start Node:",self.start)
        print(self.solution)
        print("-----------------------------------------------------------------")

    def computeMinCost_getChild(self,v):
        minCost=0
        childList={}
        childList[minCost]=[]
        flag=True   #at the beginning

        for nodeTupleList in self.get_neighbors(v):
            # print(nodeTupleList)
            cost=0
            new_list=[]
            for c,weight in nodeTupleList:
                cost=cost+self.get_heuristic(c)+weight
                new_list.append(c)

            if flag is True:   #outside above for
                minCost=cost
                childList[minCost]=new_list
                flag=False
            
            else:
                if minCost>cost:
                    minCost=cost
                    childList[minCost]=new_list
        return minCost,childList[minCost]

    def aoStar(self,v,backtracking):
        print("Heuristic :",self.H)
        print("Solution :",self.solution)
        print("Processing Node :",v)
        print("-------------------------------------------------------------------------")
        if self.get_status(v)>=0:
            minCost,childList=self.computeMinCost_getChild(v)
            self.set_heuristic(v,minCost)
            self.set_status(v,len(childList))
            #still inside if until end
            solved=True
            for childNode in childList:
                self.parent[childNode]=v
                if self.get_status(childNode)!=-1:
                    solved=solved & False
            
            if solved==True:
                self.set_status(v,-1)
                self.solution[v]=childList   #solution is a dictionary
            
            if v!=self.start:
                self.aoStar(self.parent[v],True)
            
            if backtracking==False:
                for childNode in childList:
                    self.set_status(childNode,0)
                    self.aoStar(childNode,False)

    def applyAOStar(self):
        self.aoStar(self.start,False)
    
    

heuristic = {'A': 1, 'B': 4, 'C': 2, 'D': 3, 'E': 6, 'F':8, 'G': 2, 'H': 0, 'I': 0, 'J': 0} # Heuristic values of Nodes
graph = {                                   # Graph of Nodes and Edges
    'A': [[('B', 1)], [('C', 1), ('D', 1)]], # Neighbors of Node 'A', B, C & D with repective weights
    'B': [[('E', 1)], [('F', 1)]],           # Neighbors are included in a list of lists
    'C': [[('G', 1)],[('H', 1), ('I', 1)]],                       # Each sublist indicate a "OR" node or "AND" nodes
    'D': [[('J', 1)]],
}
G1=Graph(heuristic,graph,"A")
G1.applyAOStar()
G1.printSolution()