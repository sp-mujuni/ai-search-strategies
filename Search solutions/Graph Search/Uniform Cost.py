from queue import PriorityQueue

def uniform_cost_search(graph, start, goal):
    queue = PriorityQueue()
    queue.put((0, start))
    expanded_states = set()
    path = {}

    while not queue.empty():
        cost, current_state = queue.get()

        if current_state == goal:
            path_cost = cost
            break

        if current_state not in expanded_states:
            expanded_states.add(current_state)
            neighbors = graph[current_state]
            sorted_neighbors = sorted(neighbors, key=lambda x: x[0])

            for neighbor, edge_cost in sorted_neighbors:
                if neighbor not in expanded_states:
                    new_cost = cost + edge_cost
                    queue.put((new_cost, neighbor))
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

start_state = 'S'
goal_state = 'G'

expanded_states, path, unexpanded_states = uniform_cost_search(python_graph, start_state, goal_state)

print("Order in which states are expanded:", list(expanded_states))
print("Path returned by graph search:", path)
print("States that are not expanded:", list(unexpanded_states))
