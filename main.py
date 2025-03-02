from src import ui, graph_traversal, file_io, profiling
from src.graph_data import GraphData
from typing import Callable


def algorithm_selector(choice: chr) -> Callable:
    char_func_map = {
        'A': graph_traversal.breadth_first_search,
        'B': graph_traversal.depth_first_search,
        'C': graph_traversal.iterative_deepening_dfs,
        'D': graph_traversal.best_first_search,
        'E': graph_traversal.a_star_search
    }

    return char_func_map[choice]


if __name__ == '__main__':

    graph = GraphData(file_io.parse_adjacencies(), file_io.parse_coords()).G
    first_iteration = True

    # program execution loop

    while (first_iteration or ui.cont()):
        first_iteration = False

        starting_town = ui.get_str("\nChoose a Starting Town:",
                                   lambda input: input in graph.nodes,
                                   f"Town Doesn't Exist\n---\nValid Towns: {graph.nodes}")
        
        ending_town = ui.get_str("Choose an Ending Town:",
                                lambda input: input in graph.nodes,
                                f"Town Doesn't Exist\n---\nValid Towns: {graph.nodes}")
        
        chosen_algorithm = algorithm_selector(ui.get_traversal_menu_option())
        profiling.get_execution_time(chosen_algorithm, 5, graph)