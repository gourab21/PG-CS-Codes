import heapq

def prims_algorithm(vertices, edges):
    """
    Prim's algorithm to find the MST.

    :param vertices: List of vertices.
    :param edges: List of edges as [weight, vertex1, vertex2].
    :return: Total weight of MST and the MST as a list of edges.
    """
    # Initialize graph adjacency list
    graph = {v: [] for v in vertices}
    for weight, u, v in edges:
        graph[u].append((v, weight))
        graph[v].append((u, weight))

    # Start with an arbitrary vertex (first in the list)
    start = vertices[0]

    # Priority queue to select minimum weight edge
    priority_queue = [(0, start, None)]  # (weight, current vertex, parent vertex)
    mst = []
    total_weight = 0
    visited = set()

    while priority_queue:
        weight, current, parent = heapq.heappop(priority_queue)

        # Skip if already visited
        if current in visited:
            continue

        # Mark current vertex as visited
        visited.add(current)

        # If not the starting vertex, add the edge to the MST
        if parent is not None:
            mst.append((parent, current, weight))
            total_weight += weight

        # Explore neighbors
        for neighbor, edge_weight in graph[current]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (edge_weight, neighbor, current))

    return total_weight, mst


# Input
edges = []
vertices = input("Enter the vertices - ").split()
n = int(input("Enter the number of edges - "))
print("Enter Edges as weight, vertex 1, vertex 2 ")
for i in range(n):
    x = input(f"Enter edge {i + 1} - ").split()
    edges.append([int(x[0]), x[1], x[2]])

# Execute Prim's algorithm
mst_weight, mst = prims_algorithm(vertices, edges)

# Output
print(f"\nTotal weight of MST: {mst_weight}")
print("Edges in the MST:")
for u, v, weight in mst:
    print(f"({u}, {v}) with weight {weight}")
