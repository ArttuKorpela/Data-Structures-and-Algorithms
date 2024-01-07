import matplotlib.pyplot as plt
import networkx as nx
from networkx.algorithms.traversal.depth_first_search import dfs_preorder_nodes
from networkx.algorithms.traversal.breadth_first_search import bfs_tree

# Define the graph from the image
edges = [('A', 'G'), ('G', 'D'), ('D', 'F'),('D', 'F'), ('F', 'H'), ('F', 'E'),
         ('E', 'J'), ('E', 'B'), ('H', 'I')]
G = nx.Graph()
G.add_edges_from(edges)

# Use NetworkX to perform depth-first search and breadth-first search
# Starting from vertex 'A'
dfs_order = list(dfs_preorder_nodes(G, 'A'))
bfs_order = list(nx.bfs_tree(G, 'A').nodes())

dfs_order, bfs_order