def depth_first_search(tree, start, goal):
    # Initialize a stack for DFS and a set to keep track of visited nodes.
    stack = [start]
    visited = set()

    # Perform DFS until the stack is empty.
    while stack:
        current_node = stack.pop()

        # Check if the current node is the goal node.
        if current_node == goal:
            return True  # Goal node found

        # Mark the current node as visited.
        visited.add(current_node)

        # Add unvisited child nodes to the stack.
        if current_node in tree:
            for child in tree[current_node]:
                if child not in visited:
                    stack.append(child)

    return False  # Goal node not found in the tree

# Testing the DFS function
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

if depth_first_search(python_graph, start_node, goal_node):
    print(f"Goal node '{goal_node}' found in the tree.")
else:
    print(f"Goal node '{goal_node}' not found in the tree.")
