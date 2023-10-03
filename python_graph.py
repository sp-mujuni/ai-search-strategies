# There are two versions of the python graph used in the python programs of the search strategies:
python_graph = {
    'S': {'A': 3, 'B': 1},
    'A': {'B': 2, 'C': 2},
    'B': {'C': 3},
    'C': {'D': 4, 'G': 4},
    'D': {'G': 1},
    'G': {}
}

python_graph = {
    'S': [('A', 3), ('B', 1)],
    'A': [('B', 2), ('C', 2)],
    'B': [('C', 3)],
    'C': [('D', 4), ('G', 4)],
    'D': [('G', 1)],
    'G': []
}
