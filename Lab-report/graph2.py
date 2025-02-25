import random

# Constants
OBSTACLE = '#'
EMPTY = '.'
SOURCE = 'S'
GOAL = 'G'
PATH = '*'

# Directions for moving in the grid
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def generate_grid(N):
    """Generate a random NxN grid with a source and goal."""
    grid = [[EMPTY for _ in range(N)] for _ in range(N)]
    
    # Randomly place source and goal
    source = (random.randint(0, N-1), random.randint(0, N-1))
    goal = (random.randint(0, N-1), random.randint(0, N-1))
    
    # Ensure source and goal are not the same and are not obstacles
    while goal == source:
        goal = (random.randint(0, N-1), random.randint(0, N-1))
    
    grid[source[0]][source[1]] = SOURCE
    grid[goal[0]][goal[1]] = GOAL
    
    # Randomly place obstacles (20% of the grid)
    for i in range(N):
        for j in range(N):
            if grid[i][j] == EMPTY and random.random() < 0.2:
                grid[i][j] = OBSTACLE
    
    return grid, source, goal

def is_valid_cell(grid, row, col):
    """Check if a cell is within the grid and not an obstacle."""
    N = len(grid)
    return 0 <= row < N and 0 <= col < N and grid[row][col] != OBSTACLE

def dfs(grid, start, goal):
    """Perform DFS to find a path from start to goal."""
    N = len(grid)
    visited = [[False for _ in range(N)] for _ in range(N)]
    parent = [[None for _ in range(N)] for _ in range(N)]
    stack = [start]
    topological_order = []
    
    while stack:
        row, col = stack.pop()
        if (row, col) == goal:
            # Reconstruct path
            path = []
            current = (row, col)
            while current is not None:
                path.append(current)
                current = parent[current[0]][current[1]]
            path.reverse()
            return path, topological_order
        
        if not visited[row][col]:
            visited[row][col] = True
            topological_order.append((row, col))
            
            # Explore neighbors in random order
            random.shuffle(DIRECTIONS)
            for dr, dc in DIRECTIONS:
                new_row, new_col = row + dr, col + dc
                if is_valid_cell(grid, new_row, new_col) and not visited[new_row][new_col]:
                    parent[new_row][new_col] = (row, col)
                    stack.append((new_row, new_col))
    
    return None, topological_order  # No path found

def print_grid(grid, path=None):
    """Print the grid, optionally marking the path."""
    N = len(grid)
    for i in range(N):
        for j in range(N):
            if path and (i, j) in path and grid[i][j] not in {SOURCE, GOAL}:
                print(PATH, end=' ')
            else:
                print(grid[i][j], end=' ')
        print()

def main():
    # Randomly choose N between 4 and 7
    N = random.randint(4, 7)
    grid, source, goal = generate_grid(N)
    
    print("Generated Grid:")
    print_grid(grid)
    print(f"Source: {source}, Goal: {goal}")
    
    # Perform DFS
    path, topological_order = dfs(grid, source, goal)
    
    if path:
        print("\nDFS Path:")
        print_grid(grid, path)
        print(f"Path: {path}")
    else:
        print("\nNo path found from source to goal.")
    
    print("\nTopological Order of Node Traversal:")
    print(topological_order)

if __name__ == "__main__":
    main()