from collections import defaultdict

class Graph:


    def __init__(self):


        self.graph = defaultdict(list)


    def addEdge(self, u, v):
        self.graph[u].append(v)


    def DFSUtil(self, v, visited):

        visited.add(v)
        print(v, end=' ')


        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)


    def DFS(self, v):

        visited = set()

        self.DFSUtil(v, visited)




g = Graph()

n = int(input("Enter no of edges to enter:"))
for i in range(n):
    a,b = map(int,input("Enter Where to add edge(Numbers seperated with space):").split())
    g.addEdge(a,b)

n = int(input("Enter Where to Start BFS From"))

"""g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
"""
print("Following is DFS starting from vertex ",n)
g.DFS(n)
