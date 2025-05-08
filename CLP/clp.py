from collections import deque
import random

def generate_grid(n, obstacles_count):
    """
    Generate an N x N grid filled with 0s and place a given number of obstacles (represented by 1s).
    Returns the grid and the set of obstacle positions.
    """
    grid = [[0 for _ in range(n)] for _ in range(n)]
    obstacle_positions = set()

    while len(obstacle_positions) < obstacles_count:
        x = random.randint(0, n - 1)
        y = random.randint(0, n - 1)

        # Ensure the same obstacle isn't placed twice
        if (x, y) not in obstacle_positions:
            grid[x][y] = 1
            obstacle_positions.add((x, y))

    return grid, obstacle_positions

def bfs(grid, start, goal):
    """
    Perform Breadth-First Search (BFS) to find the shortest path from start to goal.
    Avoids obstacles and stays within grid bounds.
    """
    n = len(grid)
    
    # Directions: (dx, dy, direction_name)
    directions = [(-1, 0, 'Up'), (1, 0, 'Down'), (0, -1, 'Left'), (0, 1, 'Right')]
    
    queue = deque([(start, [])])  # Queue stores (current_position, path_so_far)
    visited = set()
    visited.add(start)

    while queue:
        (x, y), path = queue.popleft()

        # Goal check
        if (x, y) == goal:
            return path

        # Explore all four directions
        for dx, dy, direction in directions:
            nx, ny = x + dx, y + dy

            if (0 <= nx < n) and (0 <= ny < n) and (nx, ny) not in visited:
                if grid[nx][ny] != 1:  # Not an obstacle
                    visited.add((nx, ny))
                    queue.append(((nx, ny), path + [(direction, (nx, ny))]))

    return None  # No path found

def print_moves(moves):
    """
    Nicely print the list of moves as direction and coordinates.
    """
    for direction, (x, y) in moves:
        print(f"Moving {direction} -> ({x}, {y})")

# ---------------- Main Program ----------------

if __name__ == "__main__":
    # Step 1: Input grid size and number of obstacles
    N = int(input("Enter grid size N (e.g., 5 for a 5x5 grid): "))
    obstacles_count = int(input("Enter number of obstacles to place randomly: "))

    # Step 2: Generate the grid and display it
    grid, obstacle_positions = generate_grid(N, obstacles_count)
    
    print("\nGenerated Grid (1 = obstacle, 0 = free space):")
    for row in grid:
        print(row)

    # Step 3: Take user input for start and goal positions
    start = tuple(map(int, input("\nEnter starting position (x y): ").split()))
    goal = tuple(map(int, input("Enter goal position (x y): ").split()))

    # Step 4: Run BFS to find path
    moves = bfs(grid, start, goal)

    # Step 5: Print result
    if moves:
        print("\nRequired Moves to Reach Goal:")
        print_moves(moves)
    else:
        print("\nNo path found from start to goal. It may be blocked by obstacles.")
