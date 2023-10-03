import heapq  # Import the heapq module for efficient priority queue operations.

def astar_search(graph, start, goal, heuristic):
    # Create a priority queue (heap) for A* Search and a dictionary to keep track of costs.
    priority_queue = [(0 + heuristic[start], 0, start)]  # (f_cost, g_cost, node)
    cost_so_far = {start: 0}

    # Perform A* Search until the priority queue is empty.
    while priority_queue:
        # Dequeue the node with the lowest f_cost (f_cost = g_cost + heuristic) from the priority queue.
        _, current_cost, current_node = heapq.heappop(priority_queue)

        # Check if the current node is the goal node.
        if current_node == goal:
            return current_cost  # Return the cost of the path to the goal.

        # Explore neighbors and update costs.
        for neighbor, edge_cost in graph.get(current_node, {}).items():
            total_cost = current_cost + edge_cost
            f_cost = total_cost + heuristic[neighbor]

            # If the neighbor node has not been visited or the new f_cost is lower, update the cost.
            if neighbor not in cost_so_far or total_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = total_cost
                heapq.heappush(priority_queue, (f_cost, total_cost, neighbor))

    return float('inf')  # Goal node not found in the graph; return infinity as a sentinel value.

#Testing a-star function
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

# Call the A* Search function to find the cost of the shortest path.
shortest_path_cost = astar_search(python_graph, start_node, goal_node, heuristic_values)

if shortest_path_cost != float('inf'):
    print(f"Shortest path cost from '{start_node}' to '{goal_node}': {shortest_path_cost}")
else:
    print(f"No path found from '{start_node}' to '{goal_node}'.")
