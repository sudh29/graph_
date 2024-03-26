# Graph

In a graph, Depth First Search (DFS) and Breadth First Search (BFS) algorithms are used to traverse the nodes. Here's how they work:

# Depth First Search (DFS):

DFS explores as far as possible along each branch before backtracking. It starts at a source node and explores as far as possible along each branch before backtracking.
DFS can be implemented using recursion or a stack data structure.
It visits all the vertices of a graph and for each vertex, it explores all the edges adjacent to that vertex.
DFS is often used to detect cycles in a graph.

# Breadth First Search (BFS):

BFS explores neighbors of the current vertex before moving to the next level of vertices. It starts at a source node and explores all the neighbor nodes at the present depth before moving on to the nodes at the next depth level.
BFS uses a queue data structure to keep track of the nodes to be visited next.
BFS is often used to find the shortest path between two nodes in an unweighted graph.

## Below are the Python implementations of DFS and BFS for a graph represented using an adjacency list:

```python
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    # Depth First Search (DFS) implementation
    def dfs_util(self, v, visited):
        visited[v] = True
        print(v, end=' ')
        for i in self.graph[v]:
            if not visited[i]:
                self.dfs_util(i, visited)

    def dfs(self, v):
        visited = [False] * (len(self.graph))
        self.dfs_util(v, visited)

    # Breadth First Search (BFS) implementation
    def bfs(self, v):
        visited = [False] * (len(self.graph))
        queue = []
        queue.append(v)
        visited[v] = True

        while queue:
            v = queue.pop(0)
            print(v, end=' ')
            for i in self.graph[v]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

# Example usage:
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

# Code

```python
from collections import defaultdict

class Graph():
    def __init__(self):
        self.graph = defaultdict(list)
        
    def add_edge(self,u,v):
        self.graph[u].append(v)
    
    def print_graph(self):
        print(self.graph)

def solve_dfs(val,visited,graph):
    visited[val] = True
    print(val,end=' ')
    for i in graph[val]:
        if not visited[i]:
            solve_dfs(i,visited,graph)
            
def dfs(val,graph):
    visited = [False]*len(graph)
    solve_dfs(val,visited,graph)
    

def bfs(val,graph):
    visited = [False]*len(graph)
    q = []
    q.append(val)
    visited[val]=True
    while q:
        val = q.pop(0)
        print(val,end=' ')
        for i in graph[val]:
            if not visited[i]:
                q.append(i)
                visited[i]=True
    
# Example usage:
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

g.print_graph()
dfs(2,g.graph)
print()
bfs(2,g.graph)

    
```

print("DFS Traversal:")
g.dfs(2)  # Output: 2 0 1 3
print("\nBFS Traversal:")
g.bfs(2)  # Output: 2 0 3 1

```
