
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



  def show(self):
    print(self.graphDict)

  def Dijkstras_Shortest_Path(self, src):

    distance = [9999999999] * self.vertCount
    distance[src] = 0

graph = SimpleGraph(directed=True)

graph.addVertex(1)
graph.addVertex(2)
graph.addVertex(3)
graph.addVertex(4)

graph.addEdge(1, 2, 1)
graph.addEdge(1, 3, 2)
graph.addEdge(2, 3, 1)
graph.addEdge(2, 4, 3)
graph.addEdge(3, 4, 4)
graph.addEdge(4, 1, 5)
graph.show()