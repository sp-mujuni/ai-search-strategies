from collections import deque  # Import the deque class for efficient queue operations.

def breadth_first_search(graph, start, goal):
    # Create a queue for BFS and a set to keep track of visited nodes.
    queue = deque([start])  # Initialize the queue with the start node.
    visited = set()  # Initialize the set for visited nodes.

    # Perform BFS until the queue is empty.
    while queue:
        current_node = queue.popleft()  # Dequeue the front node.

        # Check if the current node is the goal node.
        if current_node == goal:
            return True  # Goal node found

        # Mark the current node as visited.
        visited.add(current_node)

        # Enqueue unvisited neighbors.
        for neighbor in graph[current_node]:
            if neighbor not in visited and neighbor not in queue:
                queue.append(neighbor)

    return False  # Goal node not found in the graph.

#Testing BFS function
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

# Call the BFS function to search for the goal node.
found_goal = breadth_first_search(python_graph, start_node, goal_node)

if found_goal:
    print(f"Goal node '{goal_node}' found in the graph.")
else:
    print(f"Goal node '{goal_node}' not found in the graph.")
