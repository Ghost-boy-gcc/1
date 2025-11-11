#Graph Traversal (DFS and BFS) Implementation
from collections import deque

#Using Adjacency Matrix
locations = ['A', 'B', 'C', 'D']
location_index = {name: idx for idx, name in enumerate(locations)}

adj_matrix = [
    [0, 1, 1, 0],  # A
    [0, 0, 0, 1],  # B
    [1, 0, 0, 1],  # C
    [0, 1, 1, 0]   # D
]

def dfs_matrix(start):
    visited = [False] * len(locations)
    result = []
    
    def dfs(node_idx):
        visited[node_idx] = True
        result.append(locations[node_idx])
        for neighbor_idx in range(len(locations)):
            if adj_matrix[node_idx][neighbor_idx] == 1 and not visited[neighbor_idx]:
                dfs(neighbor_idx)
    
    dfs(location_index[start])
    return result

#Using Adjacency List
adj_list = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

def bfs_list(start):
    visited = set()
    queue = deque([start])
    result = []
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node)
            for neighbor in adj_list.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)
    return result

#Menu System
def menu():
    print("\n==== Menu ====")
    print("1. DFS")
    print("2. BFS")
    print("3. Exit")

if __name__ == "__main__":
    while True:
        menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            start_location = 'A'
            dfs_result = dfs_matrix(start_location)
            print(f"DFS Traversal (using adjacency matrix): {dfs_result}")
        elif choice == '2':
            start_location = 'A'
            bfs_result = bfs_list(start_location)
            print(f"BFS Traversal (using adjacency list): {bfs_result}")
        elif choice == '3':
            break