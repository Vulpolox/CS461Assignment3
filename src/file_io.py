from pathlib import Path
import csv

adj_path = Path(__file__).resolve().parent / 'data' / 'Adjacencies.txt'
coord_path = Path(__file__).resolve().parent / 'data' / 'coordinates.csv'

def parse_coords() -> list:
    output = []
    with open(coord_path, mode='r') as file:
        coords_file = csv.reader(file)
        for location in coords_file:
            output.append((location[0], [location[1], location[2]]))
    return output


def parse_adjacencies() -> list:
    output = []
    with open(adj_path, mode='r') as file:
        adj_file = csv.reader(file, delimiter=' ')
        for adj_pair in adj_file:
            output.append((adj_pair[0], adj_pair[1]))
    return output


def process_files() -> None:
    pass