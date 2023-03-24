class GraphNode:
    def __init__(self, item=None):
        self.item=item

class Edge():
    def __init__(self, node1,node2,weight=0):
        self.node1=node1
        self.node2=node2
        self.weight=weight


class Graph():
    def __init__(self):
        self.nodes = {}
        self.size=0

    def neighbors(self, v):
        #Returns list of neighbors of vertex v1
        if v not in self.nodes.keys():
            return 
        neighboringVertices = []
        for edge in self.nodes[v]:
            neighboringVertices.append(edge.node2)
        return neighboringVertices

    def inDegree(self, v):
        #Returns number of incoming edges at vertex v
        inDegreeCount = 0
        for vertex in self.nodes.keys():
            for edge in self.nodes[vertex]:
                if edge.node2 == v:
                    inDegreeCount +=1
        return inDegreeCount

    def allVertices(self):
        verticesSet = set()
        verticesList = []
        for vertex in self.nodes.keys():
            for edge in self.nodes[vertex]:
                if(edge.node1 not in verticesSet):
                    verticesList.append(edge.node1)
                    verticesSet.add(edge.node1)
                if(edge.node2 not in verticesSet):
                    verticesList.append(edge.node2)
                    verticesSet.add(edge.node2)
        return verticesList

    def DFS_pre(self, start):
        stack = []
        visited = set()
        stack.append(start)

        dfs = []

        while stack:
            currentNode = stack.pop()
            if currentNode not in visited:
                dfs.append(currentNode)
                visited.add(currentNode)

                for neighbor in self.neighbors(currentNode):
                    if neighbor not in visited: 
                        stack.append(neighbor)
        return dfs
    
    def DFS_pre_rec(self, start):
        visited = set()
        dfs = []
        self.DFS_pre_rec_helper(start,visited,dfs)
        return dfs

    def DFS_pre_rec_helper(self,start,visited, dfs):
        dfs.append(start)
        visited.add(start)
        
        for vertex in self.neighbors(start):
            if vertex not in visited:
                self.DFS_pre_rec_helper(vertex,visited, dfs)
    
    def DFS_post(self,start):
        visited = set()
        dfs = []
        self.DFS_post_rec_helper(start,visited,dfs)
        return dfs

    def DFS_post_rec_helper(self,start,visited, dfs):
        visited.add(start)
        
        for vertex in self.neighbors(start):
            if vertex not in visited:
                self.DFS_pre_rec_helper(vertex,visited, dfs)
        dfs.append(start)

    def topologicalSort(self,start):
        dfsPostOrder = self.DFS_post(start)
        return dfsPostOrder[::-1]

    def BFS(self, start):
        queue = []
        visited = set()
        queue.append(start)
        bfs = []

        while queue:
            currentNode = queue.pop(0)
            if currentNode not in visited:
                visited.add(currentNode)
                bfs.append(currentNode)

                for neighbor in self.neighbors(currentNode):
                    if neighbor not in visited:
                        queue.append(neighbor)
        
        return bfs

    def addEdge(self, v1, v2,weight=0):
        #Adds an edge to the graph
        if v1 not in self.nodes.keys():
            self.nodes[v1] = [Edge(v1,v2,weight)]
        else:
            self.nodes[v1].append(Edge(v1, v2, weight))

    def addUndirectedEdge(self, v1, v2, weight=0):
        self.addEdge(v1, v2,weight)
        self.addEdge(v2, v1,weight)
    
    def isAdjacent(self, v1, v2):
        #Returns True if there is an edge from v1 to v2
        if v1 in self.nodes:
            for edge in self.nodes[v1]:
                if edge.node2 == v2:
                    return True
        if v2 in self.nodes:
            for edge in self.nodes[v2]:
                if edge.node2 == v1:
                    return True
        return False
        
    def print(self):
        for key in self.nodes.keys():
            printThis = str(key) + " -> "+str([[edge.node2] for edge in self.nodes[key]])
            print(printThis)



def testing():
    g = Graph()
    g.addUndirectedEdge(0, 1)
    g.addUndirectedEdge(0, 3)
    g.addUndirectedEdge(0, 2)
    g.addUndirectedEdge(1,3)
    g.addUndirectedEdge(2, 3)
    g.addUndirectedEdge(3, 4)
    g.addUndirectedEdge(2, 5)
    g.addUndirectedEdge(5, 6)
    #g.addUndirectedEdge(5, 6)
    #g.print()
    #print(g.isAdjacent(5 , 6))
    #print(g.neighbors(7))
    #print(g.inDegree(3))
    #print(g.allVertices())
    print(g.DFS_pre(0))
    print(g.DFS_pre_rec(0))
    print(g.DFS_post(0))
    print(g.topologicalSort(0))
    print(g.BFS(0))
if __name__ == "__main__":
    testing()