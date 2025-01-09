import heapq

def prims_algorithm(vertices, edges):
    """
    Implements Prim's Algorithm to find the MST of a graph using a min-heap.
    
    Parameters:
    vertices (list): List of vertices in the graph.
    edges (list): List of edges, where each edge is represented as
                  (weight, u, v).
    
    Returns:
    tuple: A tuple containing:
           - The total weight of the MST.
           - The list of edges in the MST.
    """
    # Build the adjacency list
    graph = {v: [] for v in vertices}
    for weight, u, v in edges:
        graph[u].append((weight, v))
        graph[v].append((weight, u))

    # Initialize structures
    visited = set()
    mst = []
    mst_weight = 0

    # Min-heap to pick the smallest edge
    min_heap = [(0, vertices[0], None)]  # (weight, current_vertex, parent)

    while min_heap and len(visited) < len(vertices):
        weight, current, parent = heapq.heappop(min_heap)  # Extract the minimum edge

        if current in visited:
            continue

        visited.add(current)

        # If the edge is part of the MST, add it
        if parent is not None:
            mst.append((parent, current, weight))
            mst_weight += weight

        # Add all edges from the current vertex to the min-heap
        for edge_weight, neighbor in graph[current]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, neighbor, current))

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
             (14, 'd', 'f')
    ]
    '''edges = []
    vertices = [i for i in input("Enter the vertices - ").split()]
    n = int(input("Enter the number of edges - "))
    print("Enter Edges as weight, vertex 1, vertex 2 ")
    for i in range(n):
        x = input(f"Enter edge {i + 1} - ").split()
        edges.append([int(x[0]), x[1], x[2]])
        '''
    mst_weight, mst = prims_algorithm(vertices, edges)
    print(f"Total weight of MST: {mst_weight}")
    print("Edges in the MST:")
    for u, v, weight in mst:
        print(f"({u}, {v}) with weight {weight}")
