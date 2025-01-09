def dfs(graph, start, visited=None, path=None):
    if visited is None:
        visited = set()  # Initialize the visited set
    if path is None:
        path = []  # Initialize the path list

    # Mark the current node as visited
    visited.add(start)
    path.append(start)
    print(start, end=" ")  # Print the node or perform any action

    # Recur for all the vertices adjacent to this vertex
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, path)

    return path

def dfs_all(graph):
    visited = set()  # To track all visited nodes
    all_paths = []   # To store paths for disconnected components

    # Iterate through all nodes in the graph
    for node in graph:
        if node not in visited:
            print(f"\nStarting new DFS from node {node}:")
            path = dfs(graph, node, visited)
            all_paths.append(path)
    
    return all_paths

# Example Usage:
if __name__ == "__main__":
    # Graph represented as an adjacency list
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E'],
        'G': ['H'],  # A disconnected component
        'H': ['G']
    }
    g = {
    'u': ['v', 'x'],  # 'u' has directed edges to 'v' and 'x'
    'v': ['y'],       # 'v' has a directed edge to 'y'
    'w': ['y', 'z'],     # 'w' has a directed edge to 'z'
    'x': ['v'],       # 'x' has a directed edge to 'v'
    'y': ['x'],  # 'y' has directed edges to 'x' and 'z'
    'z': ['z']        # 'z' has a self-loop (edge to itself)
}


       
    


    print("DFS Traversal for the entire graph:")
    all_paths = dfs_all(g)

    print("\n\nPaths for all components:")
    for i, path in enumerate(all_paths):
        print(f"Component {i + 1}: {' -> '.join(path)}")

