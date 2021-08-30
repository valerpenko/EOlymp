
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


graph = Graph(5, directed=False)

graph.addEdge(0, 1, 4)
graph.addEdge(1, 4, 3)
graph.addEdge(2, 1, 2)
graph.addEdge(3, 0, 1)
graph.addEdge(4, 2, 2)
graph.show()