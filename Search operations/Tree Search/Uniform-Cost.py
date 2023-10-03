import heapq  # Import the heapq module for efficient priority queue operations.

def uniform_cost_search(tree, start, goal):
    # Initialize a priority queue (heap) for UCS and a dictionary to keep track of costs.
    priority_queue = [(0, start)]  # Each element is a tuple (cost, node).
    cost_dict = {start: 0}

    # Perform UCS until the priority queue is empty.
    while priority_queue:
        # Dequeue the node with the lowest cost from the priority queue.
        current_cost, current_node = heapq.heappop(priority_queue)

        # Check if the current node is the goal node.
        if current_node == goal:
            return current_cost  # Return the cost of the path to the goal.

        # Explore child nodes and update costs.
        for child_node, edge_cost in tree.get(current_node, []):
            total_cost = current_cost + edge_cost

            # If the child node has not been visited or the new cost is lower, update the cost.
            if child_node not in cost_dict or total_cost < cost_dict[child_node]:
                cost_dict[child_node] = total_cost
                heapq.heappush(priority_queue, (total_cost, child_node))

    return float('inf')  # Goal node not found in the tree; return infinity as a sentinel value.

# Testing the UCS function
python_graph = {
    'S': [('A', 3), ('B', 1)],
    'A': [('B', 2), ('C', 2)],
    'B': [('C', 3)],
    'C': [('D', 4), ('G', 4)],
    'D': [('G', 1)],
    'G': []
}

start_node = 'S'
goal_node = 'G'

shortest_path_cost = uniform_cost_search(python_graph, start_node, goal_node)
if shortest_path_cost != float('inf'):
    print(f"Shortest path cost from '{start_node}' to '{goal_node}': {shortest_path_cost}")
else:
    print(f"No path found from '{start_node}' to '{goal_node}'.")
