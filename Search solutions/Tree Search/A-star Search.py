from queue import PriorityQueue

def astar_search(graph, heuristic_values, start, goal):
    queue = PriorityQueue()
    queue.put((heuristic_values[start], start))
    g_values = {state: float('inf') for state in graph}
    g_values[start] = 0
    expanded_states = set()
    path = {}

    while not queue.empty():
        _, current_state = queue.get()

        if current_state == goal:
            path_cost = g_values[goal]
            break

        if current_state not in expanded_states:
            expanded_states.add(current_state)
            neighbors = graph[current_state]

            for neighbor, edge_cost in neighbors:
                if neighbor not in expanded_states:
                    tentative_g = g_values[current_state] + edge_cost
                    if tentative_g < g_values[neighbor]:
                        g_values[neighbor] = tentative_g
                        f_value = tentative_g + heuristic_values[neighbor]
                        queue.put((f_value, neighbor))
                        path[neighbor] = current_state

    unexpanded_states = set(graph.keys()) - expanded_states

    # Reconstruct the path
    if goal in path:
        current = goal
        final_path = [current]
        while current != start:
            current = path[current]
            final_path.append(current)
        final_path.reverse()
    else:
        final_path = []

    return expanded_states, final_path, unexpanded_states

python_graph = {
    'S': [('A', 3), ('B', 1)],
    'A': [('B', 2), ('C', 2)],
    'B': [('C', 3)],
    'C': [('D', 4), ('G', 4)],
    'D': [('G', 1)],
    'G': []
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

expanded_states, path, unexpanded_states = astar_search(python_graph, heuristic_values, start_state, goal_state)

print("Order in which states are expanded:", list(expanded_states))
print("Path returned by tree search:", path)
print("States that are not expanded:", list(unexpanded_states))
