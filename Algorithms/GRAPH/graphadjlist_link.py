# Define a class for linked list nodes
class Node:
    def __init__(self, vertex):
        self.vertex = vertex  # Store vertex
        self.next = None      # Pointer to the next node


# Define a class for the adjacency list representation of the graph
class AdjList:
    def __init__(self):
        self.head = None  # Initialize the head of the linked list as None


# Define a class for the Graph
class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        # Create an array of adjacency lists. Size of the array is the number of vertices
        self.adjacency_list = [AdjList() for _ in range(self.V)]

    # Add an edge to the graph (directed)
    def add_edge(self, src, dest):
        # Add node to the adjacency list of src
        node = Node(dest)
        node.next = self.adjacency_list[src].head
        self.adjacency_list[src].head = node

    # Print the graph as adjacency lists
    def print_graph(self):
        for i in range(self.V):
            print(f"Adjacency list of vertex {i}:", end="")
            temp = self.adjacency_list[i].head
            while temp:
                print(f" -> {temp.vertex}", end="")
                temp = temp.next
            print()


# Example usage
g = Graph(4)  # Create a graph with 4 vertices (0, 1, 2, 3)

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

g.print_graph()
