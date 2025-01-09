def dfs(graph,vertex):
    visited = set()
    dfs_order = []
    dfs_recursive(graph, vertex, visited, dfs_order)
    return dfs_order

def dfs_recursive(graph, vertex, visited, dfs_order):
    # Initialize visited set and DFS order list
    
    visited.add(vertex)  # Mark the current vertex as visited
    dfs_order.append(vertex)  # Add the vertex to the DFS order

    # Recur for all neighbors of the current vertex
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, dfs_order)
    

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
        graph[j].append(i) #undirected graph
    

# Input the starting vertex for DFS
start_vertex = input("Enter the starting vertex for DFS - ")

#global Variables.


# Perform DFS
dfs_order=dfs(graph, start_vertex)

# Output the DFS traversal order
print("DFS Traversal Order:", dfs_order)
