import networkx as nx
import matplotlib.pyplot as plt

def plotgraph(name,adj):
    # Create a graph object using networkx
    G = nx.Graph()
    for i in name:
        # Add nodes to the graph
        G.add_node(i)

    for i in range(len(adj)):
        for j in range(len(adj)):
            if adj[i][j]==1:
                # Add edges between nodes
                G.add_edge(name[i],name[j])
    
    # Draw the graph
    plt.figure(figsize=(8, 6))
    nx.draw(G, with_labels=True, node_color='skyblue', node_size=1500, font_size=20, font_color='black', edge_color='gray', linewidths=2)
    plt.title("Graph Visualization", size=15)
    plt.show()
