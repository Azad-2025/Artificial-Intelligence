def is_valid(x, y, grid, visited):
    rows, cols = len(grid), len(grid[0])
    return 0 <= x < rows and 0 <= y < cols and grid[x][y] == 0 and not visited[x][y]

def depth_limited_search(x, y, target, depth, grid, visited, path, traversal):
    if depth < 0:
        return False
    if (x, y) == target:
        path.append((x, y))
        traversal.append((x, y))
        return True

    visited[x][y] = True
    traversal.append((x, y))

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny, grid, visited):
            if depth_limited_search(nx, ny, target, depth - 1, grid, visited, path, traversal):
                path.append((x, y))
                return True

    return False

def iddfs(grid, start, target, max_depth=50):
    for depth in range(max_depth):
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        path = []
        traversal = []

        if depth_limited_search(start[0], start[1], target, depth, grid, visited, path, traversal):
            print(f"Path found at depth {depth} using IDDFS")
            print("Traversal Order:", traversal)
            print("Path:", list(reversed(path)))
            return

    print(f"No path found up to depth {max_depth} using IDDFS")

# --------------------------
# Test Cases
# --------------------------

print("Case 1:")
grid1 = [
    [0, 0, 1, 0],
    [1, 0, 1, 0],
    [0, 0, 0, 0],
    [1, 1, 0, 1]
]
start1 = (0, 0)
target1 = (2, 3)
iddfs(grid1, start1, target1)

print("\nCase 2:")
grid2 = [
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 0]
]
start2 = (0, 0)
target2 = (2, 2)
iddfs(grid2, start2, target2, max_depth=6)
