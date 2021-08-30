
class SimpleGraph:

  def __init__(self, directed = False):
    self.graphDict = {}
    self.directed = directed
    self.vertCount = 0

  def addVertex(self,v):
    if v in self.graphDict:
      print("Vertex ", v, " already exists.")
    else:
      self.graphDict[v] = []
      self.vertCount = self.vertCount + 1

  def addEdge(self, src, dest, weight):
    newEdge = [dest, weight]
    if src not in self.graphDict:
      print(src, " not in graph.")
    elif dest not in self.graphDict:
      print(dest, " not in graph.")
    elif self.directed:
      self.graphDict[src].append(newEdge)
    else:
      self.graphDict[src].append(newEdge)
      newEdge2 = [src, weight]
      self.graphDict[dest].append(newEdge2)

  def decWeight(self, src, dest):
    #decrements weight between src and dest by 1
    for value in self.graphDict[src]:
      if value[0] == dest:
        value[1] = value[1] - 1

  def getWeight(self, src, dest):#weight
    for value in self.graphDict[src]:
      if value[0] == dest:
        return value[1]

  def edgesFrom(self,src):
    #list with [dest node,weight]
    return self.graphDict[src]
  def show(self):
    print(self.graphDict)

  def Dijkstras_Shortest_Path(self, src):
    distance = [9999999999] * self.vertCount
    distance[src] = 0

    for u in self.graphDict:
      for [v,w] in self.edgesFrom(u):
        if distance[u] != 9999999999 and distance[u] + w < distance[v]:
          distance[v] = distance[u] + w
    return distance

  def BellmanFord(self, src):

    distance = [9999999999] * self.vertCount
    distance[src] = 0

    for u in self.graphDict:
      for [v,w] in self.graphDict[u]:
        if distance[u] != 9999999999 and distance[u] + w < distance[v]:
          distance[v] = distance[u] + w

    # for src in self.graphDict:
    #   for [v,w] in self.graphDict[src]:
    #     if distance[src] != 9999999999 and distance[src] + w < distance[v]:
    #       print("Graph contains negative cycle")

    return distance

# N=7
# M=11
# graph = SimpleGraph(directed=True)
#
# for node in range(1,N+1):
#   graph.addVertex(node)
# for node in range(2, N + 1):
#   graph.addEdge(1, node, N*N//5+1)
#
# graph.show()
# src = 2
# dest = src + 1
# for step in range(N,M+1):
#   if dest<N+1:
#     graph.addEdge(src, dest, 1)
#     graph.decWeight(1, src)
#     dest+=1
#   else:
#     src+=1
#     dest=dest+1
#     graph.addEdge(src, dest, 1)
#     graph.decWeight(1, src)
# graph.show()

graph = SimpleGraph(directed=True)
graph.addVertex(0)
graph.addVertex(1)
graph.addVertex(2)
graph.addVertex(3)
graph.addVertex(4)
graph.addEdge(0, 1, 4)
#graph.addEdge(1, 0, 3)
graph.addEdge(1, 4, 3)
graph.addEdge(2, 1, 2)
graph.addEdge(3, 0, 1)
graph.addEdge(2, 4, 2)
graph.addEdge(2, 3, 5)
graph.show()
print(graph.Dijkstras_Shortest_Path(2))
