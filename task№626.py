
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
    #x=self.graphDict[src]
    pass

  def getWeight(self, src, dest, weight):
    #!!!
    pass

  def show(self):
    print(self.graphDict)

  def Dijkstras_Shortest_Path(self, src):

    distance = [9999999999] * self.vertCount
    distance[src] = 0


N=7
M=11
graph = SimpleGraph(directed=True)

for node in range(1,N+1):
  graph.addVertex(node)
for node in range(2, N + 1):
  graph.addEdge(1, node, N*N//5+1)

graph.show()
src=2
dest=src_+1
for step in range(N,M+1):
  if dest<N+1:
    graph.addEdge(src, dest, 1)
    decWeight(1, src)
    dest+=1
  else:
    src+=1
    dest=dest+1
    graph.addEdge(src, dest, 1)
    decWeight(1, src)
