import networkx as nx

class GraphData:

    locations = set()

    def __init__(self, adj_list, coords_list):
        self.adj_list = adj_list
        self.coords_list = coords_list
        self._populate_locations()

    
    def _populate_locations(self):
        for item in self.adj_list:
            self.locations.add(item[0])
