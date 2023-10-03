def greedy_search(graph, start, goal, heuristic):
    # Create a priority queue (heap) for Greedy Search.
    priority_queue = [(heuristic[start], start)]  # (heuristic, node)

    # Perform Greedy Search until the priority queue is empty.
    while priority_queue:
        # Dequeue the node with the lowest heuristic value from the priority queue.
        _, current_node = priority_queue.pop(0)  # Ignore the heuristic value for Greedy Search.

        # Check if the current node is the goal node.
        if current_node == goal:
            return True  # Goal node found

        # Enqueue unvisited neighbors with their heuristic values.
        for neighbor, _ in graph.get(current_node, {}).items():
            if neighbor not in priority_queue:
                priority_queue.append((heuristic[neighbor], neighbor))

        # Sort the priority queue based on heuristic values (greedy choice).
        priority_queue.sort(key=lambda x: x[0])

    return False  # Goal node not found in the graph.

#Testing Greedy Search function
python_graph = {
    'S': {'A': 3, 'B': 1},
    'A': {'B': 2, 'C': 2},
    'B': {'C': 3},
    'C': {'D': 4, 'G': 4},
    'D': {'G': 1},
    'G': {}
}

start_node = 'S'  
goal_node = 'G'

# Heuristic values for each node
heuristic_values = {
    'S': 7,
    'A': 5,
    'B': 7,
    'C': 4,
    'D': 1,
    'G': 0
}

# Call the Greedy Search function to search for the goal node.
found_goal = greedy_search(python_graph, start_node, goal_node, heuristic_values)

if found_goal:
    print(f"Goal node '{goal_node}' found in the graph.")
else:
    print(f"Goal node '{goal_node}' not found in the graph.")
