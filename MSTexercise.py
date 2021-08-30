
class Graph:

    def __init__(self, vertCount, directed = False):
        self.graphMatrix = []
        self.vertCount = vertCount
        self.directed = directed
        for i in range(vertCount):
            self.graphMatrix.append([0 for i in range(vertCount)])

    def addEdge(self, vert1, vert2, weight):
        if vert1 == vert2:
            self.graphMatrix[vert1][vert2] = 0
        elif self.directed:
            self.graphMatrix[vert1][vert2] = weight
        else:
            self.graphMatrix[vert1][vert2] = weight
            self.graphMatrix[vert2][vert1] = weight

    def show(self):
        for row in self.graphMatrix:
            print(row)

def Update(Q,D):
    # обновляет Q на основании D
    # в Q должны находиться номера вершин в порядке возрастания их D
    pass
def MST_Prim_Jarnik(graph):
    Infinity=100000000
    D= graph.vertCount*[Infinity]
    D[0]=0
    Q=[i for i in range(0,len(D))]
    S=0
    while len[Q]>0:
        #RemoveMin
        u=Q[0]
        Q=Q[1:]
        #for each edge e′ = (u,v) such that v is in Q do
           if graph.graphMatrix[u,v]<D[v]:
               if D[v]==Infinity:
                   D[v]=graph.graphMatrix[u,v]
                   S+=D[v]
               else:
                   S=S-D[v]+graph.graphMatrix[u,v]
                   D[v] = graph.graphMatrix[u, v]
        Update(Q,D)
    return S
    
graph = Graph(5, directed=False)

graph.addEdge(0, 1, 4)
graph.addEdge(1, 4, 3)
graph.addEdge(2, 1, 2)
graph.addEdge(3, 0, 1)
graph.addEdge(4, 2, 2)
graph.show()
print(MST_Prim_Jarnik(graph))