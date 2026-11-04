import networkx as nx

G = nx.Graph()
edges = [('S0', 'S1', 11), ('S0', 'S2', 20), ('S1', 'S2', 8), ('S1', 'S3', 15), ('S3', 'S4', 8), ('S2', 'S4', 15), ('S1', 'S4', 21), ('S2', 'S5', 9), ('S4', 'S5', 7), ('S3', 'S6', 16), ('S4','S7', 19), ('S6', 'S7', 9), ('S5', 'S7', 19)]
G.add_weighted_edges_from(edges)
distances = nx.single_source_dijkstra_path_length(G, source='S0')
print("Shortest distances from S0:", distances)
