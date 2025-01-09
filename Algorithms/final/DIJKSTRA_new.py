import heapq

def initialize_single_source(vertices, start):
    """
    Initializes the distances and predecessors for Dijkstra's algorithm.
    """
    distances = {v: float('inf') for v in vertices}  # Distance to all nodes is infinity
    predecessors = {v: None for v in vertices}  # Predecessors are initially None
    distances[start] = 0  # Distance to the source is 0
    return distances, predecessors

def relax(u, v, weight, distances, predecessors):
    """
    Performs the relaxation step to update distance and predecessor.
    """
    if distances[u] + weight < distances[v]:
        distances[v] = distances[u] + weight
        predecessors[v] = u

def dijkstra_algorithm(vertices, edges, start):
    """
    Implements Dijkstra's algorithm using the pseudocode structure.

    Parameters:
    vertices (list): List of vertices in the graph.
    edges (list): List of edges represented as (weight, vertex1, vertex2).
    start (str): The source vertex.

    Returns:
    tuple: (distances, predecessors)
           - distances: Dictionary of shortest distances from source.
           - predecessors: Dictionary of predecessors for shortest paths.
    """
    # Step 1: Initialize distances and predecessors
    distances, predecessors = initialize_single_source(vertices, start)

    # Step 2: Build adjacency list
    graph = {v: [] for v in vertices}
    for weight, u, v in edges:
        graph[u].append((v, weight))
        # graph[v].append((u, weight))  # Uncomment if the graph is undirected

    # Step 3: Initialize priority queue
    priority_queue = [(distances[start], start)]  # (distance, vertex)
    print(priority_queue)
    visited = set()  # Set to track visited nodes

    while priority_queue:
        # Step 4: Extract vertex with minimum distance
        current_distance, u = heapq.heappop(priority_queue)
        if u in visited:
            continue
        visited.add(u)

        # Step 5: Relax adjacent vertices
        for v, weight in graph[u]:
            if v not in visited:
                old_distance = distances[v]
                relax(u, v, weight, distances, predecessors)
                if distances[v] < old_distance:  # If distance is updated, push to queue
                    heapq.heappush(priority_queue, (distances[v], v))

    return distances, predecessors


# Input
edges = []
vertices = []
n = int(input("Enter the number of edges - "))
print("Enter Edges as weight, vertex 1, vertex 2 ")
for i in range(n):
    x = input(f"Enter edge {i + 1} - ").split()
    edges.append([int(x[0]), x[1], x[2]])
    vertices.append(x[1])
    vertices.append(x[2])
vertices = list(set(vertices))
start_vertex = input("Enter the source vertex - ")

# Execute Dijkstra's algorithm
distances, predecessors = dijkstra_algorithm(vertices, edges, start_vertex)

# Output
print(f"\nShortest distances from vertex {start_vertex}:")
for vertex, distance in distances.items():
    print(f"Vertex {vertex}: Distance = {distance}")

print("\nPredecessors for each vertex:")
for vertex, predecessor in predecessors.items():
    print(f"Vertex {vertex}: Predecessor = {predecessor}")
