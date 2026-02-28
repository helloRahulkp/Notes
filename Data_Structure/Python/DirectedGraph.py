from collections import deque

class DirectedGraph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {i: [] for i in range(vertices)}

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def print_graph(self):
        for key in self.graph:
            print(f"Vertex {key}:", " -> ".join(map(str, self.graph[key])))

    # DFS
    def dfs_util(self, v, visited):
        visited[v] = True
        print(v, end=" ")
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.dfs_util(neighbor, visited)

    def dfs(self, start):
        visited = [False] * self.V
        print(f"DFS starting from vertex {start}: ", end="")
        self.dfs_util(start, visited)
        print()

    # BFS
    def bfs(self, start):
        visited = [False] * self.V
        queue = deque([start])
        visited[start] = True
        print(f"BFS starting from vertex {start}: ", end="")
        while queue:
            v = queue.popleft()
            print(v, end=" ")
            for neighbor in self.graph[v]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        print()

# Driver code
if __name__ == "__main__":
    g = DirectedGraph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 4)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 0)

    g.print_graph()
    g.dfs(0)
    g.bfs(0)