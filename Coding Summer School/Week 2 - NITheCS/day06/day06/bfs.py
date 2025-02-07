# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 15:18:18 2025

@author: Lehlo
"""
from collections import deque

def bfs_shortest_path(graph, start, goal):
    queue = deque([[start]])
    visited = set([start])
    
    while queue:
        path = queue.popleft()
        node = path[-1]
        
        if node == goal:
            return path  # Found it
        
        for neighbor in graph.get(node, []):
            if neighbor not in visited:  # Fixed syntax error
                visited.add(neighbor)
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                
    return None  # No path found

def main():
    example_graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"]
    }
    
    start_node = "A"
    goal_node = "F"
    
    path = bfs_shortest_path(example_graph, start_node, goal_node)
    if path:
        print(f"Shortest path from {start_node} to {goal_node}: {path}")
    else:
        print("No path found")

# Ensure the script runs properly
if __name__ == "__main__":  
    main()
