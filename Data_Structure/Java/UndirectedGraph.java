import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;



class Graph {
    private int vertices;
    private LinkedList<Integer>[] adjList;

    // Constructor to create graph
    public Graph(int vertices) {
        this.vertices = vertices;
        adjList = new LinkedList[vertices];

        for (int i = 0; i < vertices; i++) {
            adjList[i] = new LinkedList<>();
        }
    }

    // Add an undirected edge
    public void addEdge(int src, int dest) {
        adjList[src].add(dest);
        adjList[dest].add(src); // because undirected
    }

    // Remove an undirected edge
    public void removeEdge(int src, int dest) {
        adjList[src].remove(Integer.valueOf(dest));
        adjList[dest].remove(Integer.valueOf(src));
    }

    // Display the graph
    public void displayGraph() {
        System.out.println("\n--- Graph Adjacency List ---");
        for (int i = 0; i < vertices; i++) {
            System.out.print("Vertex " + i + ":");
            for (Integer v : adjList[i]) {
                System.out.print(" -> " + v);
            }
            System.out.println();
        }
    }

    // DFS Traversal
    public void DFS(int startVertex) {
        boolean[] visited = new boolean[vertices];
        System.out.print("\nDFS Traversal starting from vertex " + startVertex + ": ");
        DFSUtil(startVertex, visited);
        System.out.println();
    }

    private void DFSUtil(int vertex, boolean[] visited) {
        visited[vertex] = true;
        System.out.print(vertex + " ");

        for (int neighbor : adjList[vertex]) {
            if (!visited[neighbor]) {
                DFSUtil(neighbor, visited);
            }
        }
    }

    // BFS Traversal
    public void BFS(int startVertex) {
        boolean[] visited = new boolean[vertices];
        Queue<Integer> queue = new LinkedList<>();

        visited[startVertex] = true;
        queue.offer(startVertex);

        System.out.print("\nBFS Traversal starting from vertex " + startVertex + ": ");

        while (!queue.isEmpty()) {
            int vertex = queue.poll();
            System.out.print(vertex + " ");

            for (int neighbor : adjList[vertex]) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    queue.offer(neighbor);
                }
            }
        }
        System.out.println();
    }
}

public class UndirectedGraph {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number of vertices: ");
        int V = sc.nextInt();

        Graph graph = new Graph(V);
        int choice;

        while (true) {
            System.out.println("\n--- Undirected Graph Operations ---");
            System.out.println("1. Add Edge");
            System.out.println("2. Remove Edge");
            System.out.println("3. Display Graph");
            System.out.println("4. DFS Traversal");
            System.out.println("5. BFS Traversal");
            System.out.println("6. Exit");
            System.out.print("Enter your choice: ");
            choice = sc.nextInt();

            switch (choice) {
                case 1:
                    System.out.print("Enter source and destination: ");
                    int src = sc.nextInt();
                    int dest = sc.nextInt();
                    graph.addEdge(src, dest);
                    break;
                case 2:
                    System.out.print("Enter source and destination: ");
                    src = sc.nextInt();
                    dest = sc.nextInt();
                    graph.removeEdge(src, dest);
                    break;
                case 3:
                    graph.displayGraph();
                    break;
                case 4:
                    System.out.print("Enter starting vertex for DFS: ");
                    int startDFS = sc.nextInt();
                    graph.DFS(startDFS);
                    break;
                case 5:
                    System.out.print("Enter starting vertex for BFS: ");
                    int startBFS = sc.nextInt();
                    graph.BFS(startBFS);
                    break;
                case 6:
                    sc.close();
                    System.exit(0);
                default:
                    System.out.println("Invalid choice!");
            }
        }
    }
}
