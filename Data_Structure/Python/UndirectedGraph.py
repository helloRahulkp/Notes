from collections import deque

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj_list = {i: [] for i in range(vertices)}

    # Add undirected edge
    def add_edge(self, src, dest):
        if dest not in self.adj_list[src]:
            self.adj_list[src].append(dest)
        if src not in self.adj_list[dest]:
            self.adj_list[dest].append(src)

    # Remove undirected edge
    def remove_edge(self, src, dest):
        if dest in self.adj_list[src]:
            self.adj_list[src].remove(dest)
        if src in self.adj_list[dest]:
            self.adj_list[dest].remove(src)

    # Display the graph
    def display_graph(self):
        print("\n--- Graph Adjacency List ---")
        for vertex, neighbors in self.adj_list.items():
            print(f"{vertex}: {' -> '.join(map(str, neighbors))}")

    # DFS traversal
    def dfs(self, start):
        visited = [False] * self.V
        print(f"\nDFS Traversal starting from vertex {start}: ", end="")
        self._dfs_util(start, visited)
        print()

    def _dfs_util(self, vertex, visited):
        visited[vertex] = True
        print(vertex, end=" ")

        for neighbor in self.adj_list[vertex]:
            if not visited[neighbor]:
                self._dfs_util(neighbor, visited)

    # BFS traversal
    def bfs(self, start):
        visited = [False] * self.V
        queue = deque()

        visited[start] = True
        queue.append(start)

        print(f"\nBFS Traversal starting from vertex {start}: ", end="")

        while queue:
            vertex = queue.popleft()
            print(vertex, end=" ")

            for neighbor in self.adj_list[vertex]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        print()


# Main program
if __name__ == "__main__":
    V = int(input("Enter number of vertices: "))
    graph = Graph(V)

    while True:
        print("\n--- Undirected Graph Operations ---")
        print("1. Add Edge")
        print("2. Remove Edge")
        print("3. Display Graph")
        print("4. DFS Traversal")
        print("5. BFS Traversal")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            src = int(input("Enter source: "))
            dest = int(input("Enter destination: "))
            graph.add_edge(src, dest)

        elif choice == 2:
            src = int(input("Enter source: "))
            dest = int(input("Enter destination: "))
            graph.remove_edge(src, dest)

        elif choice == 3:
            graph.display_graph()

        elif choice == 4:
            start = int(input("Enter starting vertex for DFS: "))
            graph.dfs(start)

        elif choice == 5:
            start = int(input("Enter starting vertex for BFS: "))
            graph.bfs(start)

        elif choice == 6:
            print("Exiting...")
            break

        else:
            print("Invalid choice! Please try again.")