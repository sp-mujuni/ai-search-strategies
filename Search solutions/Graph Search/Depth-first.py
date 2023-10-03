def depth_first_search(graph, start, goal):
    stack = [(start, [start])]
    expanded_states = set()
    path = []

    while stack:
        current_state, current_path = stack.pop()

        if current_state == goal:
            path = current_path
            break

        if current_state not in expanded_states:
            expanded_states.add(current_state)
            neighbors = graph[current_state]
            sorted_neighbors = sorted(neighbors.keys())

            for neighbor in reversed(sorted_neighbors):
                if neighbor not in expanded_states:
                    new_path = current_path + [neighbor]
                    stack.append((neighbor, new_path))

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

start_state = 'S'
goal_state = 'G'

expanded_states, path, unexpanded_states = depth_first_search(python_graph, start_state, goal_state)

print("Order in which states are expanded:", list(expanded_states))
print("Path returned by graph search:", path)
print("States that are not expanded:", list(unexpanded_states))
