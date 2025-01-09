import heapq

def dijkstra_algorithm(vertices, edges, start):
   
    # Initialize graph adjacency list
    graph = {v: [] for v in vertices}
    for weight, u, v in edges:
        graph[u].append((v, weight))

    # Initialize distances and priority queue
    distances = {v: float('inf') for v in vertices}
    predecessors = {v: None for v in vertices}
    distances[start] = 0

    priority_queue = [(0, start)]  # (distance, vertex)

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Skip if a better distance is already recorded
        if current_distance > distances[current_vertex]:
            continue

        # Relax adjacent vertices
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))

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
vertices=list(set(vertices))

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

