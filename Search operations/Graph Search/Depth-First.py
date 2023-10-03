def depth_first_search(graph, start, goal):
    # Create a stack for DFS and a set to keep track of visited nodes.
    stack = [start]  # Initialize the stack with the start node.
    visited = set()  # Initialize the set for visited nodes.

    # Perform DFS until the stack is empty.
    while stack:
        current_node = stack.pop()  # Pop the last node from the stack.

        # Check if the current node is the goal node.
        if current_node == goal:
            return True  # Goal node found

        # Mark the current node as visited.
        visited.add(current_node)

        # Explore neighbors and push unvisited neighbors onto the stack.
        for neighbor in graph[current_node]:
            if neighbor not in visited and neighbor not in stack:
                stack.append(neighbor)

    return False  # Goal node not found in the graph.

# Testing DFS function
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

# Call the DFS function to search for the goal node.
found_goal = depth_first_search(python_graph, start_node, goal_node)

if found_goal:
    print(f"Goal node '{goal_node}' found in the graph.")
else:
    print(f"Goal node '{goal_node}' not found in the graph.")
