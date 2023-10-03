import heapq  # Import the heapq module for efficient priority queue operations.

def astar_search(tree, start, goal, heuristic):
    # Initialize a priority queue (heap) for A* Search and a dictionary to keep track of costs.
    priority_queue = [(heuristic[start], 0, start)]  # (heuristic, cost_so_far, node)
    cost_so_far = {start: 0}

    # Perform A* Search until the priority queue is empty.
    while priority_queue:
        # Dequeue the node with the lowest combined cost (heuristic + cost_so_far).
        _, current_cost, current_node = heapq.heappop(priority_queue)

        # Check if the current node is the goal node.
        if current_node == goal:
            return current_cost  # Return the cost of the path to the goal.

        # Explore child nodes.
        for child_node, edge_cost in tree.get(current_node, []):
            total_cost = current_cost + edge_cost + heuristic[child_node]

            # If the child node has not been visited or the new cost is lower, update the cost.
            if child_node not in cost_so_far or total_cost < cost_so_far[child_node]:
                cost_so_far[child_node] = total_cost
                heapq.heappush(priority_queue, (total_cost, total_cost, child_node))

    return float('inf')  # Goal node not found in the tree; return infinity as a sentinel value.

# Testing the a-star function
python_graph = {
    'S': [('A', 3), ('B', 1)],
    'A': [('B', 2), ('C', 2)],
    'B': [('C', 3)],
    'C': [('D', 4), ('G', 4)],
    'D': [('G', 1)],
    'G': []
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

shortest_path_cost = astar_search(python_graph, start_node, goal_node, heuristic_values)
if shortest_path_cost != float('inf'):
    print(f"Shortest path cost from '{start_node}' to '{goal_node}': {shortest_path_cost}")
else:
    print(f"No path found from '{start_node}' to '{goal_node}'.")
