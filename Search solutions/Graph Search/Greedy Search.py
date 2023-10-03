from queue import PriorityQueue

def greedy_search(graph, heuristic_values, start, goal):
    queue = PriorityQueue()
    queue.put((heuristic_values[start], start))
    expanded_states = set()
    path = []

    while not queue.empty():
        _, current_state = queue.get()

        if current_state == goal:
            path = [current_state]
            break

        if current_state not in expanded_states:
            expanded_states.add(current_state)
            neighbors = graph[current_state]
            sorted_neighbors = sorted(neighbors.keys())

            for neighbor in sorted_neighbors:
                if neighbor not in expanded_states:
                    queue.put((heuristic_values[neighbor], neighbor))

    unexpanded_states = set(graph.keys()) - expanded_states

    return expanded_states, path, unexpanded_states

python_graph = {
    'S': {'A': 3, 'B': 1},
    'A': {'B': 2, 'C': 2},
    'B': {'C': 3},
    'C': {'D': 4, 'G': 4},
    'D': {'G': 1},
    'G': {}
}

heuristic_values = {
    'S': 7,
    'A': 5,
    'B': 7,
    'C': 4,
    'D': 1,
    'G': 0
}

start_state = 'S'
goal_state = 'G'

expanded_states, path, unexpanded_states = greedy_search(python_graph, heuristic_values, start_state, goal_state)

print("Order in which states are expanded:", list(expanded_states))
print("Path returned by graph search:", path)
print("States that are not expanded:", list(unexpanded_states))
