def greedy_search(tree, start, goal, heuristic):
    # Initialize a priority queue (heap) for Greedy Search.
    priority_queue = [(heuristic[start], start)]  # Each element is a tuple (heuristic, node)

    # Perform Greedy Search until the priority queue is empty.
    while priority_queue:
        # Dequeue the node with the lowest heuristic value from the priority queue.
        _, current_node = priority_queue.pop(0)  # Ignore the heuristic value for Greedy Search.

        # Check if the current node is the goal node.
        if current_node == goal:
            return True  # Goal node found

        # Explore child nodes.
        for child_node in tree.get(current_node, []):
            # Enqueue child nodes with their heuristic values.
            priority_queue.append((heuristic[child_node], child_node))

        # Sort the priority queue based on heuristic values (greedy choice).
        priority_queue.sort(key=lambda x: x[0])

    return False  # Goal node not found in the tree.

# Testing the Greedy Search function
python_graph = {
    'S': {'A': 3, 'B': 1},
    'A': {'B': 2, 'C': 2},
    'B': {'C': 3},
    'C': {'D': 4, 'G': 4},
    'D': {'G': 1},
    'G': {}
}

# Heuristic values for each node
heuristic_values = {
    'S': 7,
    'A': 5,
    'B': 7,
    'C': 4,
    'D': 1,
    'G': 0
}

start_node = 'S'
goal_node = 'G'

found_goal = greedy_search(python_graph, start_node, goal_node, heuristic_values)
if found_goal:
    print(f"Goal node '{goal_node}' found in the tree.")
else:
    print(f"Goal node '{goal_node}' not found in the tree.")
