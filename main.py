my_graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('A', 4), ('C', 1), ('D', 5)],
    'C': [('A', 2), ('B', 1), ('D', 8), ('E', 10)],
    'D': [('B', 5), ('C', 8), ('E', 2)],
    'E': [('C', 10), ('D', 2)]
}



def shortest_path_finder(graph, start_node):

    # Create a list of unvisited nodes
    unvisited_nodes = list(graph)

    # Create a dictionary of node weights. 
    # Assign weight of 0 for the start node, and the rest an infinity value.
    node_weights = {key: 0 if key == start_node else float("inf") for key in graph}

    # Create a "paths" dictionary to track the shortest path to the target node.
    shortest_paths = {key: [] for key in graph}

    # For the start node, append the start node
    shortest_paths[start_node].append(start_node)


    # While unvisited_nodes has at least one item:
    while unvisited_nodes:

        # Get the node with the smallest node (Explore the node with the smallest node first)
        current_node = min(unvisited_nodes, key=node_weights.get)

        # For the neighbour node:
        for node, distance in graph[current_node]:

            # Check if the total distance to the currenly explored node is smaller than the weight of currently explored node:
            # In other words, this is checking if there is a better path to the currently explored node
            if distance + node_weights[current_node] < node_weights[node]:
                
                # Update the currently explored node weight with that value (new smaller weight)
                node_weights[node] = distance + node_weights[current_node]

                # Check if the currently explored node already has a path to that node:
                # This means that the path needs to be updated with the better (shorter) path
                if shortest_paths[node] and shortest_paths[node][-1] == node:
                    shortest_paths[node] = shortest_paths[current_node][:]

                else:
                    # If the currently explored node has no path or incomplete path
                    # Add the shortest path of the current node to the shortest path of the currently explored node
                    shortest_paths[node].extend(shortest_paths[current_node])
                
                # Append the currently explored node to the path
                shortest_paths[node].append(node)
        
        # Remove the already visited node from the unviisited_nodes
        unvisited_nodes.remove(current_node)
    
    
    # Display the result
    print("\n")
    print(f"Distances From Start Node to Each Node:")
    print(f"---------------------------------------")
    for key, value in shortest_paths.items():
        print(f'{start_node} - {key} shortest path distance: {node_weights[key]}')
        print(f'Path: {" -> ".join(shortest_paths[key])}\n')
 
    return node_weights, shortest_paths




shortest_path_finder(my_graph, "A")