def find_path(network, start, end):
    # Keep track of visited nodes to avoid cycles
    visited = set()
    
    def dfs(current, path):
        # If we've reached the end node, we've found a path
        if current == end:
            return path
        
        # Mark current node as visited
        visited.add(current)
        
        # Try each unvisited neighbor
        for neighbor in network[current]:
            if neighbor not in visited:
                result = dfs(neighbor, path + [neighbor])
                if result is not None:
                    return result
        
        return None
    
    # Start the search from the start node
    return dfs(start, [start])

def main():
    # Test network from the example
    network = {
        'A': {'B', 'C'},
        'B': {'D', 'E'},
        'C': {'D'},
        'D': {'E'},
        'E': set()
    }

    # Test cases
    print(find_path(network, 'A', 'E'))  # Could return ['A', 'B', 'E'] or ['A', 'C', 'D', 'E']
    print(find_path(network, 'A', 'A'))  # Returns ['A']
    print(find_path(network, 'E', 'A'))  # Returns None (no path exists from E to A)

if __name__ == '__main__':
    main() 