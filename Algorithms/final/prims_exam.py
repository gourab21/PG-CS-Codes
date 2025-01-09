import heapq

class Vertex:
    """
    A class to represent a vertex with properties:
    - key: Minimum weight edge connecting this vertex to the MST.
    - parent: The parent vertex in the MST.
    """
    def __init__(self, id):
        self.id = id
        self.key = float('inf')
        self.parent = None

def prims_algorithm(vertices, edges):
    """
    Implements Prim's Algorithm to find the MST of a graph based on the MST-PRIM pseudocode.

    Parameters:
    vertices (list): List of vertex IDs.
    edges (list): List of edges, where each edge is represented as (weight, u, v).

    Returns:
    tuple: A tuple containing:
           - The total weight of the MST.
           - The list of edges in the MST.
    """
    # Initialize graph adjacency list
    graph = {v: [] for v in vertices}
    for weight, u, v in edges:
        graph[u].append((weight, v))
        graph[v].append((weight, u))

    # Create vertex objects
    vertex_objects = {v: Vertex(v) for v in vertices}

    # Select an arbitrary start vertex
    r = vertices[0]
    vertex_objects[r].key = 0

    # Min-heap priority queue
    min_heap = [(v.key, v.id) for v in vertex_objects.values()]
    heapq.heapify(min_heap)

    mst_weight = 0
    mst_edges = []
    in_mst = set()

    while min_heap:
        # Extract the vertex with the smallest key
        _, u = heapq.heappop(min_heap)

        # Skip if the vertex is already part of the MST
        if u in in_mst:
            continue
        in_mst.add(u)

        # Update MST weight and edges
        mst_weight += vertex_objects[u].key
        if vertex_objects[u].parent is not None:
            mst_edges.append((vertex_objects[u].parent, u, vertex_objects[u].key))

        # Relax edges and update keys
        for weight, v in graph[u]:
            if v not in in_mst and weight < vertex_objects[v].key:
                vertex_objects[v].key = weight
                vertex_objects[v].parent = u
                heapq.heappush(min_heap, (vertex_objects[v].key, v))

    return mst_weight, mst_edges


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
             (14, 'd', 'f')]
    edges = []
    vertices = [i for i in input("Enter the vertices - ").split()]
    n = int(input("Enter the number of edges - "))
    print("Enter Edges as weight, vertex 1, vertex 2 ")
    for i in range(n):
        x = input(f"Enter edge {i + 1} - ").split()
        edges.append([int(x[0]), x[1], x[2]])
    
    mst_weight, mst = prims_algorithm(vertices, edges)
    print(f"Total weight of MST: {mst_weight}")
    print("Edges in the MST:")
    for u, v, weight in mst:
        print(f"({u}, {v}) with weight {weight}")
