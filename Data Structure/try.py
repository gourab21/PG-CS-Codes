import networkx as nx
import matplotlib.pyplot as plt

# Create a graph object using networkx
G = nx.Graph()

# Add nodes to the graph
G.add_node("A")
G.add_node("B")
G.add_node("C")
G.add_node("D")

# Add edges between nodes
G.add_edge("A", "B")
G.add_edge("B", "A")
G.add_edge("A", "A")
G.add_edge("A", "C")
G.add_edge("B", "D")
G.add_edge("C", "D")

# Draw the graph
plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_color='skyblue', node_size=1500, font_size=20, font_color='black', edge_color='gray', linewidths=2)
plt.title("Graph Visualization", size=15)
plt.show()
