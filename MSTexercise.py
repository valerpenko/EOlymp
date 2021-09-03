def Update(Q,D):
    # обновляет Q на основании D
    # в Q должны находиться номера вершин в порядке возрастания их D
    Q2=[Q[0]]
    for i in range(1,len(Q)):
        if  D[i]<D[Q2[0]]:
            Q2.insert(0, Q[i])  # в начало
        else:
            Q2.append(Q[i])
    Q=Q2

def MST_Prim_Jarnik(graphMatrix):
    Infinity=100000000
    D= len(graphMatrix)*[Infinity]
    D[0]=0
    Q=[i for i in range(0,len(D))]
    S=0
    while len[Q]>0:
        #RemoveMin
        u=Q[0]
        Q=Q[1:]
        #for each edge e′ = (u,v) such that v is in Q do
        for v in Q:
           if graphMatrix[u][v]>0 and graphMatrix[u][v]<D[v]:  #v u ???
               if D[v]==Infinity:
                   D[v]=graphMatrix[u][v]
                   S+=D[v]
               else:
                   S=S-D[v]+graphMatrix[u][v]
                   D[v] = graphMatrix[u, v]
        Update(Q,D)
    return S

[vertices, edges] = map(int, input().split())
graphMatrix=[ [ 0 for col in range(0,vertices)] for row in range(0,vertices) ]
for i in range(0,edges):
    [vertice1, vertice2, weight] = map(int, input().split())
    graphMatrix[vertice1-1][vertice2-1]=weight
print(MST_Prim_Jarnik(graphMatrix))