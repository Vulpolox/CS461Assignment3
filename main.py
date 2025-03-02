from src import ui, graph_traversal, file_io
from src.graph_data import GraphData

if __name__ == '__main__':

    graph = GraphData(file_io.parse_adjacencies(), file_io.parse_coords()).G