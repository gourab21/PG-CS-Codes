import draw

class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        self.names=[]
        # Create a V x V matrix initialized to 0
        self.adjacency_matrix = [[0 for _ in range(self.V)] for _ in range(self.V)]

    # Add an edge to the graph (directed)
    def add_edge(self, src, dest):
        # Set the matrix element to 1 to indicate an edge from src to dest
        self.adjacency_matrix[src][dest] = 1

    # For undirected graphs, use this method to add an edge in both directions
    def add_undirected_edge(self, src, dest):
        # Set matrix elements in both directions
        self.adjacency_matrix[src][dest] = 1
        self.adjacency_matrix[dest][src] = 1

    # Print the adjacency matrix
    def print_matrix(self):
        for row in self.adjacency_matrix:
            print(row)
            
def directed():
    n=int(input("Enter Number of Vertices - "))
    g = Graph(n)
    for i in range(n):
        t=input("Enter name of edge "+str(i)+" - ")
        g.names.append(t)
        
    
    print("Enter 1 for an edge between two vertices and anything else if absent.")
    for i in range(n):
        for j in range(n):
            a=input("Enter 1 for an edge between "+g.names[i]+" and "+g.names[j]+" - ")
            if a=='1':
                g.add_edge(i,j)

    g.print_matrix()
    return g

def undirected():
    n=int(input("Enter Number of Vertices - "))
    g = Graph(n)
    for i in range(n):
        t=input("Enter name of edge "+str(i)+" - ")
        g.names.append(t)
    
    print("Enter 1 for an edge between two vertices and anything else if absent.")
    for i in range(n):
        for j in range(n):
            if g.adjacency_matrix[j][i]!=1 and j>=i:
                a=input("Enter 1 for an edge between "+g.names[i]+" and "+g.names[j]+" - ")
                if a=='1':
                    g.add_undirected_edge(i,j)

    g.print_matrix()
    return g



a=int(input("1. Directed Graph  2. Undirected Graph"))
if a==1:
    g=directed()
    draw.plotgraph(g.names,g.adjacency_matrix)
    
elif a==2:
    g=undirected()
    draw.plotgraph(g.names,g.adjacency_matrix)




'''
g = Graph(4)  # Create a graph with 4 vertices (0, 1, 2, 3)

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

g.print_matrix()'''

