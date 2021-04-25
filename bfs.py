from collections import defaultdict
class Graph:

    # Constructor
    def __init__(self):

        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):

        visited = [False] * (max(self.graph) + 1)

        queue = []


        queue.append(s)
        visited[s] = True

        while queue:

            s = queue.pop(0)
            print(s, end=" ")

            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True



g = Graph()
n = int(input("Enter no of edges to enter:"))
for i in range(n):
    a,b = map(int,input("Enter Where to add edge(Numbers seperated with space):").split())
    g.addEdge(a,b)

n = int(input("Enter Where to Start BFS From"))
"""
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
"""
print("Following is Breadth First Traversal starting from vertex ",n)
g.BFS(n)
