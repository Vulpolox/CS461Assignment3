import networkx as nx, math, time
from collections import deque

def breadth_first_search(graph: nx.Graph) -> None:
    total_distance: float = 0.0


def depth_first_search(graph: nx.Graph) -> None:
    pass


def iterative_deepening_dfs(graph: nx.Graph) -> None:
    pass


def best_first_search(graph: nx.Graph) -> None:
    pass


def a_star_search(graph: nx.Graph) -> None:
    pass


def distance(graph: nx.Graph, node_1, node_2) -> float:
    x1, y1 = graph.nodes[node_1]['pos']
    x2, y2 = graph.nodes[node_2]['pos']
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)