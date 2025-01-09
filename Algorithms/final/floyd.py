def floyd_warshall_with_input(vertices, edges):
    """
    Implements the Floyd-Warshall algorithm using edge-based input.
    
    Parameters:
    vertices (set): Set of vertices in the graph.
    edges (list): List of edges where each edge is represented as (source, destination, weight).
    
    Returns:
    dict: Dictionary of shortest distances between all pairs of vertices.
          If a negative weight cycle exists, returns None.
    """
    # Initialize the distance dictionary
    INF = float('inf')
    dist = {u: {v: INF for v in vertices} for u in vertices}
    
    # Distance to self is 0
    for v in vertices:
        dist[v][v] = 0
    
    # Initialize distances based on edges
    for u, v, weight in edges:
        dist[u][v] = weight

    # Apply Floyd-Warshall algorithm
    for k in vertices:
        for i in vertices:
            for j in vertices:
                if dist[i][k] != INF and dist[k][j] != INF:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    # Check for negative weight cycles
    for v in vertices:
        if dist[v][v] < 0:
            print("Graph contains a negative weight cycle")
            return None

    return dist


# Input the graph details using edges
edges = []
vertices = set()
n = int(input("Enter the number of edges: "))
print("Enter Edges as source, destination, weight")
for i in range(n):
    edge_input = input(f"Enter edge {i + 1}: ").split()
    source, destination, weight = edge_input[0], edge_input[1], int(edge_input[2])
    edges.append((source, destination, weight))
    vertices.add(source)
    vertices.add(destination)

# Running Floyd-Warshall algorithm on the graph
shortest_paths = floyd_warshall_with_input(vertices, edges)

# Output the result
if shortest_paths:
    print("Shortest path distances between all pairs of vertices:")
    for u in vertices:
        for v in vertices:
            if shortest_paths[u][v] == float('inf'):
                print(f"Distance from {u} to {v}: INF")
            else:
                print(f"Distance from {u} to {v}: {shortest_paths[u][v]}")
