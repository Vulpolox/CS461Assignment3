import networkx as nx, math, time
from collections import deque

def breadth_first_search(graph: nx.Graph, start, target) -> None:
    q = deque()
    visited = set()
    parent_map = {}

    print(f'start: {start}, end: {target}')
    print(f'neighbors of start:{list(graph.neighbors(start))}')
    return

    q.append(start)
    visited.add(start)
    parent_map[start] = None

    while not len(q) == 0:
        current_node = q.popleft()

        if current_node == target:
            results = process_path(parent_map, graph, target)
            print(f'\n---\nFound Path: {results[0]}\nPath Length: {results[1]}\n---\n')
            return

        for neighbor in graph.neighbors(current_node):
            if neighbor not in visited:
                q.append(neighbor)
                visited.add(neighbor)
                parent_map[neighbor] = current_node

    print('No path exists')

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


def process_path(parent_map: dict, graph: nx.Graph, target) -> tuple:
    path = []
    current_node = target
    total_distance = 0.0

    while current_node is not None:
        next_node = parent_map[current_node]
        path.append(current_node)

        if next_node is not None:
            total_distance += distance(graph, current_node, next_node)

        current_node = next_node

    return (path.reverse(), total_distance)