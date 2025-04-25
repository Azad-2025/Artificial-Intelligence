import random

def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def assign_clusters(points, centers):
    assignments = []
    for point in points:
        distances = [manhattan(point, center) for center in centers]
        closest_center = distances.index(min(distances))
        assignments.append(closest_center)
    return assignments

def update_centers(points, assignments, num_clusters):
    new_centers = []
    for i in range(num_clusters):
        cluster_points = [pt for pt, cluster in zip(points, assignments) if cluster == i]
        if cluster_points:
            avg_x = sum(p[0] for p in cluster_points) // len(cluster_points)
            avg_y = sum(p[1] for p in cluster_points) // len(cluster_points)
            new_centers.append((avg_x, avg_y))
        else:

            new_centers.append((random.randint(0, 39), random.randint(0, 39)))
    return new_centers

def print_grid(points, centers, grid_size=40):
    grid = [[" " for _ in range(grid_size)] for _ in range(grid_size)]

    for x, y in points:
        grid[y][x] = 'o'

    for x, y in centers:
        grid[y][x] = 'X'

    print("\nVisual Representation of Clustered Data (X = center, o = point):\n")
    for row in reversed(grid):
        print("".join(row))

def main():
    print("Enter number of data points (recommended: 100):")
    num_points = int(input())

    print("Enter number of clusters (recommended: 10):")
    num_clusters = int(input())

    points = [(random.randint(0, 39), random.randint(0, 39)) for _ in range(num_points)]
    centers = [(random.randint(0, 39), random.randint(0, 39)) for _ in range(num_clusters)]

    for iteration in range(100):
        assignments = assign_clusters(points, centers)
        new_centers = update_centers(points, assignments, num_clusters)
        if new_centers == centers:
            break
        centers = new_centers

    print_grid(points, centers)

    print("\nCluster Assignment for Each Point:\n")
    for i, (x, y) in enumerate(points):
        print(f"Point {i+1}: ({x}, {y}) -> Cluster {assignments[i] + 1}")

    print("\nFinal Cluster Centers:\n")
    for i, (x, y) in enumerate(centers):
        print(f"Cluster {i+1} Center: ({x}, {y})")

    print("\n=== Clustering Complete ===\n")

if __name__ == "__main__":
    main()
