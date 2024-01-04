def aStar(start,stop):
    open_set=set(start)
    closed_set=set()
    g={}
    parent={}

    g[start]=0
    parent[start]=start

    while len(open_set)>0:
        n=None

        for v in open_set:
            if n==None or g[v]+heuristic(v)<g[n]+heuristic(n):
                n=v
        
        if n==stop or Graph_Nodes[n]==None:
            pass
        else :
            for (m,weight) in get_neighbors(n):
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parent[m]=n
                    g[m]=g[n]+weight

                else :
                    if  g[m]<g[n]+weight:
                        g[m]=g[n]+weight
                        parent[m]=n

                    if m in closed_set:
                        closed_set.remove(m)
                        open_set.add(m)
        
        if n==None:
            print("Path not found")
            return None
        
        if n==stop:
            path=[]

            while parent[n]!=n:
                path.append(n)
                n=parent[n]
            
            path.append(start)
            path.reverse()
            print("Path found is:",path)
            return path
        
        open_set.remove(n)
        closed_set.add(n)

    print("Path not found")
    return None

def heuristic(n):
    H={
        'A': 10,
        'B': 8,
        'C': 5,
        'D': 7,
        'E': 3,
        'F': 6,
        'G': 5,
        'H': 3,
        'I': 1,
        'J': 0
        }
    return H[n]


def get_neighbors(node):
    if Graph_Nodes[node]!=None:
        return Graph_Nodes[node]
    return None

Graph_Nodes={
    'A': [('B', 6), ('F', 3)],
    'B': [('C', 3), ('D', 2)],
    'C': [('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 8)],
    'E': [('I', 5), ('J', 5)],
    'F': [('G', 1),('H', 7)] ,
    'G': [('I', 3)],
    'H': [('I', 2)],
    'I': [('E', 5), ('J', 3)]
}
aStar('A','J')