import networkx as nx

class GraphData:

    G = nx.Graph()

    def __init__(self, adj_list, coords_list):
        self.adj_list = adj_list
        self.coords_list = coords_list
        self._create_graph()


    def _create_graph(self) -> None:
        
        # add location-coordinate pairs to graph
        for location_cord_pair in self.coords_list:
            self.G.add_node(location_cord_pair)

        # add adjacencies to graph
        for adjacency in self.adj_list:
            self.G.add_edge(adjacency[0], adjacency[1])