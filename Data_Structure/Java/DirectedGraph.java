import java.util.*;
import java.util.LinkedList;
import java.util.Queue;

class DirectedGraph {
    private int V;
    private LinkedList<Integer>[] adjList;

    DirectedGraph(int V) {
        this.V = V;
        adjList = new LinkedList[V];
        for (int i = 0; i < V; i++)
            adjList[i] = new LinkedList<>();
    }

    void addEdge(int u, int v) {
        adjList[u].add(v);
    }

    void printGraph() {
        for (int i = 0; i < V; i++) {
            System.out.print("Vertex " + i + ":");
            for (int v : adjList[i])
                System.out.print(" -> " + v);
            System.out.println();
        }
    }

    // DFS
    void DFSUtil(int v, boolean[] visited) {
        visited[v] = true;
        System.out.print(v + " ");
        for (int n : adjList[v])
            if (!visited[n])
                DFSUtil(n, visited);
    }

    void DFS(int start) {
        boolean[] visited = new boolean[V];
        System.out.print("DFS starting from vertex " + start + ": ");
        DFSUtil(start, visited);
        System.out.println();
    }

    // BFS
    void BFS(int start) {
        boolean[] visited = new boolean[V];
        Queue<Integer> queue = new LinkedList<>();
        visited[start] = true;
        queue.add(start);

        System.out.print("BFS starting from vertex " + start + ": ");
        while (!queue.isEmpty()) {
            int v = queue.poll();
            System.out.print(v + " ");
            for (int n : adjList[v]) {
                if (!visited[n]) {
                    visited[n] = true;
                    queue.add(n);
                }
            }
        }
        System.out.println();
    }

    public static void main(String[] args) {
        DirectedGraph graph = new DirectedGraph(5);

        graph.addEdge(0, 1);
        graph.addEdge(0, 4);
        graph.addEdge(1, 2);
        graph.addEdge(2, 3);
        graph.addEdge(3, 0);

        graph.printGraph();
        graph.DFS(0);
        graph.BFS(0);
    }
}