def bellman_ford(edges, vertices, source):
    # Initialize distances to all vertices as infinity
    dist = {v: float('inf') for v in vertices}
    dist[source] = 0  # Distance to the source is 0

    # Relax edges |V| - 1 times
    for _ in range(len(vertices) - 1):
        for u, v, weight in edges:
            if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight

    # Check for negative weight cycles
    for u, v, weight in edges:
        if dist[u] != float('inf') and dist[u] + weight < dist[v]:
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

# Running Bellman-Ford algorithm on the graph starting from a given source node
source = input("Enter Starting Node: ")
shortest_paths = bellman_ford(edges, vertices, source)

# Output the result
if shortest_paths:
    print("Shortest distances from node", source, ":")
    for node in shortest_paths:
        print(f"Node {node}: {shortest_paths[node]}")
