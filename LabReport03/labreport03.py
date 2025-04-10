def is_color_valid(node, color, graph, colors):
    """Check if the given color can be assigned to the node."""
    return all(colors[neighbor] != color for neighbor in graph[node])

def solve_coloring(graph, max_colors, colors, node):
    """Recursive utility to solve the graph coloring problem."""
    if node == len(graph):
        return True

    for color in range(1, max_colors + 1):
        if is_color_valid(node, color, graph, colors):
            colors[node] = color
            if solve_coloring(graph, max_colors, colors, node + 1):
                return True
            colors[node] = 0  # Backtrack

    return False

def main():
    try:
        print("Enter number of vertices, edges, and colors (N M K):")
        n, m, k = map(int, input().split())

        graph = [[] for _ in range(n)]
        print(f"Enter {m} edges (u v):")
        for _ in range(m):
            u, v = map(int, input().split())
            if not (0 <= u < n and 0 <= v < n):
                print(f"Invalid edge: vertices should be between 0 and {n - 1}")
                return
            graph[u].append(v)
            graph[v].append(u)

        colors = [0] * n
        if solve_coloring(graph, k, colors, 0):
            print(f"Coloring possible with {k} colors.")
            print("Color assignment is", colors)
        else:
            print(f"Coloring not possible with {k} colors.")

    except ValueError:
        print("Invalid input! Please enter integers only.")

# Run the main function
main()
