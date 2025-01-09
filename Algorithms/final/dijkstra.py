import heapq

def add_edge(graph, weight, source, destination):
    # Adds an edge to the graph with characters as nodes
    if source not in graph:
        graph[source] = []
    if destination not in graph:
        graph[destination] = []
    graph[source].append((destination, weight))

def dijkstra(graph, source):
    # Step 1: Initialize distances and priority queue
    dist = {node: float('inf') for node in graph}  # Distance to all nodes is infinity
    dist[source] = 0  # Distance to source node is 0
    priority_queue = [(0, source)]  # Min-heap (distance, node)

    while priority_queue:
        # Step 2: Extract the node with the smallest distance
        current_distance, current_node = heapq.heappop(priority_queue)

        # Step 3: Skip if we've already found a shorter path to this node
        if current_distance > dist[current_node]:
            continue

        # Step 4: Explore neighbors
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # Step 5: Relaxation - Update distance if a shorter path is found
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))  # Add neighbor to queue with updated distance

    return dist  # Return the shortest distances from source

# Example of adding edges using add_edge function with characters
graph = {}

# Add edges to the graph: add_edge(weight, source, destination)
add_edge(graph, 1, 'A', 'B')
add_edge(graph, 4, 'A', 'C')
add_edge(graph, 2, 'B', 'C')
add_edge(graph, 5, 'B', 'D')
add_edge(graph, 1, 'C', 'D')
example=[(10, 's', 't'),
    (5, 's', 'y'),
    (1, 't', 'x'),
    (2,'t','y'),
    (9, 'y', 'x'),
    (3, 'y', 't'),
    (2, 'y', 'z'),
    (6, 'z', 'x'),
    (4,'x','z'),
    (7, 'z', 's')]
'''
graph = {}
n = int(input("Enter the number of edges - "))
print("Enter Edges as weight, source, destination ")
for i in range(n):
    x = input(f"Enter edge {i + 1} - ").split()
    add_edge(graph,int(x[0]), x[1], x[2])
'''
# Running Dijkstra's algorithm on the graph starting from node.
source = input("Enter Starting Node - ")
shortest_paths = dijkstra(graph, source)

print("Shortest distances from node", source, ":")
for node in shortest_paths:
    print(f"Node {node}: {shortest_paths[node]}")
