import networkx as nx, math, heapq
from collections import deque


def breadth_first_search(graph: nx.Graph, start, target) -> None:
    q = deque()
    visited = set()
    parent_map = {}

    q.append(start)
    visited.add(start)
    parent_map[start] = None

    while not len(q) == 0:
        current_node = q.popleft()

        if current_node == target:
            results = process_path(parent_map, graph, target)
            print(f'\n---\nFound Path: {results[0]}\nPath Length: {results[1]:.2f}\n---\n')
            return

        for neighbor in graph.neighbors(current_node):
            if neighbor not in visited:
                q.append(neighbor)
                visited.add(neighbor)
                parent_map[neighbor] = current_node

    print('\n---\nNo Path Exists\n---\n')


def depth_first_search(graph: nx.Graph, start, target) -> None:
    stack = []
    visited = set()
    parent_map = {}

    stack.append(start)
    visited.add(start)
    parent_map[start] = None

    while stack:
        current_node = stack.pop()

        if current_node == target:
            results = process_path(parent_map, graph, target)
            print(f'\n---\nFound Path: {results[0]}\nPath Length: {results[1]:.2f}\n---\n')
            return

        for neighbor in graph.neighbors(current_node):
            if neighbor not in visited:
                stack.append(neighbor)
                visited.add(neighbor)
                parent_map[neighbor] = current_node

    print('\n---\nNo Path Exists\n---\n')


def iterative_deepening_dfs(graph: nx.Graph, start, target) -> None:
    def dls(current_node, depth, visited, parent_map):
        if depth == 0:
            return False
        if current_node == target:
            return True

        for neighbor in graph.neighbors(current_node):
            if neighbor not in visited:
                visited.add(neighbor)
                parent_map[neighbor] = current_node
                if dls(neighbor, depth - 1, visited, parent_map):
                    return True
                visited.remove(neighbor)
                del parent_map[neighbor]

        return False

    depth = 0
    while True:
        visited = set()
        parent_map = {}
        visited.add(start)
        parent_map[start] = None

        if dls(start, depth, visited, parent_map):
            results = process_path(parent_map, graph, target)
            print(f'\n---\nFound Path: {results[0]}\nPath Length: {results[1]:.2f}\n---\n')
            return

        if depth > len(graph.nodes):
            print('\n---\nNo Path Exists\n---\n')
            return

        depth += 1


def best_first_search(graph: nx.Graph, start, target) -> None:
    def heuristic(node):
        return distance(graph, node, target)

    priority_queue = []
    visited = set()
    parent_map = {}

    heapq.heappush(priority_queue, (heuristic(start), start))
    visited.add(start)
    parent_map[start] = None

    while priority_queue:
        _, current_node = heapq.heappop(priority_queue)

        if current_node == target:
            results = process_path(parent_map, graph, target)
            print(f'\n---\nFound Path: {results[0]}\nPath Length: {results[1]:.2f}\n---\n')
            return

        for neighbor in graph.neighbors(current_node):
            if neighbor not in visited:
                heapq.heappush(priority_queue, (heuristic(neighbor), neighbor))
                visited.add(neighbor)
                parent_map[neighbor] = current_node

    print('\n---\nNo Path Exists\n---\n')


def a_star_search(graph: nx.Graph, start, target) -> None:
    def heuristic(node):
        return distance(graph, node, target)

    priority_queue = []
    visited = set()
    parent_map = {}
    g_score = {node: float('inf') for node in graph.nodes}
    g_score[start] = 0

    heapq.heappush(priority_queue, (heuristic(start), start))
    visited.add(start)
    parent_map[start] = None

    while priority_queue:
        _, current_node = heapq.heappop(priority_queue)

        if current_node == target:
            results = process_path(parent_map, graph, target)
            print(f'\n---\nFound Path: {results[0]}\nPath Length: {results[1]:.2f}\n---\n')
            return

        for neighbor in graph.neighbors(current_node):
            tentative_g_score = g_score[current_node] + distance(graph, current_node, neighbor)

            if tentative_g_score < g_score[neighbor]:
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic(neighbor)
                heapq.heappush(priority_queue, (f_score, neighbor))
                visited.add(neighbor)
                parent_map[neighbor] = current_node

    print('\n---\nNo Path Exists\n---\n')


def distance(graph: nx.Graph, node_1, node_2) -> float:
    x1, y1 = graph.nodes[node_1]['pos']
    x2, y2 = graph.nodes[node_2]['pos']
    x1, y1, x2, y2 = float(x1), float(y1), float(x2), float(y2)
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def process_path(parent_map: dict, graph: nx.Graph, target) -> tuple:
    path = []
    current_node = target
    total_distance = 0.0

    while current_node is not None:
        path.append(current_node)
        next_node = parent_map[current_node]

        if next_node is not None:
            total_distance += distance(graph, current_node, next_node)

        current_node = next_node

    path.reverse()
    return (path, total_distance)