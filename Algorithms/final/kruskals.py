class DisjointSet:
    """
    Implements the Disjoint Set Union (DSU) data structure
    for Kruskal's Algorithm with path compression and union by rank.
    """
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}  # Each vertex points to itself
        self.rank = {v: 0 for v in vertices}    # Initial rank is 0 for all vertices

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            # Union by rank
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def kruskal(vertices, edges):
    """
    Implements Kruskal's Algorithm to find the MST of a graph.
    Parameters:
    vertices (list): List of vertices in the graph.
    edges (list): List of edges, where each edge is represented as
                  (weight, u, v).
    Returns:
    tuple: A tuple containing:
           - The total weight of the MST.
           - The list of edges in the MST.
    """
    # Sort edges by weight
    edges.sort()

    dsu = DisjointSet(vertices)
    mst = []
    mst_weight = 0

    for weight, u, v in edges:
        # If u and v are in different components, include this edge in the MST
        if dsu.find(u) != dsu.find(v):
            dsu.union(u, v)
            mst.append((u, v, weight))
            mst_weight += weight

    return mst_weight, mst

# Example usage
if __name__ == "__main__":
    vertices = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    edges = [(1, 'g', 'h'),
            (2, 'c', 'i'),
            (2, 'f', 'g'),
            (4, 'a', 'b'),
            (4, 'c', 'f'),
            (6, 'g', 'i'),
            (7, 'c', 'd'),
            (7, 'h', 'i'),
            (8, 'a', 'h'),
            (8, 'b', 'c'),
            (9, 'd', 'e'),
            (10, 'e', 'f'),
            (11, 'b', 'h'),
             (14,'d','f')
            
    ]
    edges=[]
    vertices=[i for i in input("Enter the vertices - ").split()]
    n=int(input("Enter the number of edges - "))
    print("Enter Edges as weight, vertex 1, vertex 2 ")
    for i in range(n):
        x=input("Enter edge %i - "%(i+1)).split()
        edges.append([int(x[0]),x[1],x[2]])

    mst_weight, mst = kruskal(vertices, edges)
    print(f"Total weight of MST: {mst_weight}")
    print("Edges in the MST:")
    for u, v, weight in mst:
        print(f"({u}, {v}) with weight {weight}")
