G = nx.path_graph(7)
ORIGEM = 0
DESTINO = 6

custo, rota = nx.single_source_dijkstra(G, ORIGEM, DESTINO, weight="weight")
dist = nx.single_source_dijkstra_path_length(G, ORIGEM, weight="weight")