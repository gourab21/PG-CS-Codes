def bfs(graph,start_vertex):
        
    # Initialize BFS structures
    visited = set()  # To track visited vertices
    queue = [start_vertex]  # Regular list for the queue
    bfs_order = []  # To store the BFS traversal order

    # Perform BFS
    while queue:
        current = queue.pop(0)  # Dequeue the first element
        if current not in visited:
            visited.add(current)  # Mark it as visited
            bfs_order.append(current)  # Add to BFS order

            # Enqueue all unvisited neighbors
            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return bfs_order


# Input the graph details

graph = {}

lol=int(input("1. Directed   2. Undirected Graph. - "))
n = int(input("Enter the number of edges - "))
print("Enter Edges as vertex 1, vertex 2 ")
for i in range(n):
    x = input(f"Enter edge {i + 1} - ").split()
    i,j=x[0],x[1]
    if i not in graph:
        graph[i]=[]
    if j not in graph:
        graph[j]=[]
    graph[i].append(j)
    if lol==2:
        graph[j].append(i)
    

# Input starting vertex for BFS
start_vertex = input("Enter the starting vertex for BFS - ")

# Perform BFS and output the traversal order
bfs_result = bfs(graph, start_vertex)
print("BFS Traversal Order:", bfs_result)
