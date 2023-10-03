def breadth_first_search(tree, start, goal):
    # Initialize a queue for BFS and a set to keep track of visited nodes.
    queue = [start]
    visited = set()

    # Perform BFS until the queue is empty.
    while queue:
        current_node = queue.pop(0)  # Dequeue the front node.

        # Check if the current node is the goal node.
        if current_node == goal:
            return True  # Goal node found

        # Mark the current node as visited.
        visited.add(current_node)

        # Enqueue unvisited child nodes.
        if current_node in tree:
            for child in tree[current_node]:
                if child not in visited and child not in queue:
                    queue.append(child)

    return False  # Goal node not found in the tree

# Testing the BFS function
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

if breadth_first_search(python_graph, start_node, goal_node):
    print(f"Goal node '{goal_node}' found in the tree.")
else:
    print(f"Goal node '{goal_node}' not found in the tree.")
