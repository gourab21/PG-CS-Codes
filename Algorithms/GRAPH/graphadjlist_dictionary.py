class Graph:
    def __init__(self):
        # Dictionary to store the adjacency list
        self.adjacency_list = {}

    # Add a vertex to the graph
    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    # Add an edge to the graph (directed)
    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
        else:
            print(f"One or both vertices not found: {vertex1}, {vertex2}")

    def add_edge_undirected(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
        else:
            print(f"One or both vertices not found: {vertex1}, {vertex2}")        

    # Print the graph as an adjacency list
    def print_graph(self):
        for vertex in self.adjacency_list:
            print(f"{vertex}: {self.adjacency_list[vertex]}")


def directed():
    n=int(input("Enter Number of Vertices - "))
    g = Graph()
    for i in range(n):
        t=input("Enter name of edge "+str(i)+" - ")
        g.add_vertex(t)  
    
    print("Enter 1 for an edge between two vertices and anything else if absent.")
    x=list(g.adjacency_list.keys())
    for i in g.adjacency_list:
        for j in range(n):
            a=input("Enter 1 for an edge between "+i+" and "+x[j]+" - ")
            if a=='1':
                g.add_edge(i,x[j])

    g.print_graph()
    return g

def undirected():
    n=int(input("Enter Number of Vertices - "))
    g = Graph()
    for i in range(n):
        t=input("Enter name of edge "+str(i)+" - ")
        g.add_vertex(t)  
    
    print("Enter 1 for an edge between two vertices and anything else if absent.")
    x=list(g.adjacency_list.keys())
    for i in g.adjacency_list:
        for j in range(n):
            if x[j] not in g.adjacency_list[i]:
                a=input("Enter 1 for an edge between "+i+" and "+x[j]+" - ")
                if a=='1':
                    g.add_edge(i,x[j])
                    g.add_edge(x[j],i)

    g.print_graph()
    return g



a=int(input("1. Directed Graph  2. Undirected Graph"))
if a==1:
    g=directed()
    #draw.plotgraph(g.names,g.adjacency_matrix)
    
elif a==2:
    g=undirected()
    #draw.plotgraph(g.names,g.adjacency_matrix)

















'''
# Example usage:
g = Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')

g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'D')

g.print_graph()
'''
