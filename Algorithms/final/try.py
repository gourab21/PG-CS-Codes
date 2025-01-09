def dfs_rec(adj, visited, s, parent, dfs_tree):
    """
    Recursive DFS function to traverse and construct the DFS tree for a directed graph.
    :param adj: Dictionary adjacency list
    :param visited: Set to track visited nodes
    :param s: Current node
    :param parent: Parent node in the DFS tree
    :param dfs_tree: Dictionary to represent the DFS tree
    """
    # Mark the current vertex as visited
    visited.add(s)
    
    # Add the current node and its parent to the DFS tree
    dfs_tree[s] = parent

    # Print the current vertex
    print(s, end=" ")

    # Recursively visit all adjacent vertices
    for neighbor in adj[s]:
        if neighbor not in visited:
            dfs_rec(adj, visited, neighbor, s, dfs_tree)


def dfs(adj, s):
    """
    Perform DFS starting from a given source and construct the DFS tree for a directed graph.
    :param adj: Dictionary adjacency list
    :param s: Source node
    :return: DFS tree as a dictionary
    """
    visited = set()  # Set to track visited nodes
    dfs_tree = {}    # Dictionary to store the DFS tree
    dfs_rec(adj, visited, s, None, dfs_tree)
    return dfs_tree


def add_edge(adj, s, t):
    """
    Add a directed edge to the graph.
    :param adj: Dictionary adjacency list
    :param s: Source vertex
    :param t: Target vertex
    """
    if s not in adj:
        adj[s] = []
    if t not in adj:
        adj[t] = []
    adj[s].append(t)  # Add edge s -> t (directed)


if __name__ == "__main__":
    # Create an adjacency list for the directed graph
    adj = {}

    # Define the edges of the graph (using characters)
    edges = [('u', 'v'), ('u', 'x'), ('v', 'y'), ('w', 'y'), ('w', 'z'), ('x', 'v'), ('y', 'x')]

    # Populate the adjacency list with directed edges
    for s, t in edges:
        add_edge(adj, s, t)

    source = 'u'
    print("DFS from source:", source)
    dfs_tree = dfs(adj, source)

    print("\n\nDFS Tree:")
    for node, parent in dfs_tree.items():
        if parent is None:
            print(f"{node} (root)")
        else:
            print(f"{parent} -> {node}")
