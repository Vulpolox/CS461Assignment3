from typing import Callable


def get_char(message: str, predicate: Callable[[str], bool], error_message:str='Error: predicate eval to false') -> chr:
    in_str = input(f'{message}\n   >>>')
    
    if not len(in_str) == 0 and predicate(in_str[0]):
        return in_str[0]
    else:
        print(error_message)
        return get_str(message, predicate, error_message)


def get_str(message: str, predicate: Callable[[str], bool], error_message:str='Error: predicate eval to false') -> str:
    in_str = input(f'{message}\n   >>>')
    
    if predicate(in_str):
        return in_str
    else:
        print(error_message)
        return get_str(message, predicate, error_message)


def display_traversal_menu() -> None:
    print("""
ALGORITHMS:
   A: breadth-first search
   B: depth-first search
   C: iterative deepeing depth-first search
   D: best-first search
   E: a* search
""")
    
# === MAIN FUNCTIONS =================

def get_traversal_menu_option() -> chr:
    display_traversal_menu()
    return get_char("Choose an Algorithm", 
                    lambda c: c in ['A', 'B', 'C', 'D', 'E'], 
                    "Invalid Option.  Try Again\n-----\n")

def cont() -> bool:
    return get_char("[y] to Continue; [any key] to Quit",
                    lambda x: True,
                    "Value Entered Is Not a Char; Try Again").lower() == 'y'