from pathlib import Path
import csv

adj_path = Path(__file__).resolve().parent.parent / 'data' / 'Adjacencies.txt'
coord_path = Path(__file__).resolve().parent.parent / 'data' / 'coordinates.csv'


# output format: [(location, (x, y)), (..., (...)), ...]
def parse_coords():
    output = []
    with open(coord_path, mode='r') as file:
        coords_file = csv.reader(file)
        for location in coords_file:
            output.append((location[0], (location[1], location[2])))
    return output


# output format: [(adj_1, adj_2), (...), ...]
def parse_adjacencies() -> list:
    output = []
    with open(adj_path, mode='r') as file:
        adj_file = csv.reader(file, delimiter=' ')
        for adj_pair in adj_file:
            output.append((adj_pair[0], adj_pair[1]))
    return output