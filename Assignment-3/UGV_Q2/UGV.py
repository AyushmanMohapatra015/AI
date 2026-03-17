import numpy as np
import heapq
import random
import time
import math
import matplotlib.pyplot as plt


# Battlefield Representation :-

# 70 x 70 km battlefield
# Each grid cell represents 1 km x 1 km
GRID_SIZE = 70

# Obstacle density levels
DENSITY_LEVELS = {
    "low": 0.10,
    "medium": 0.20,
    "high": 0.35
}



# Generating Battlefield Grid with Random Obstacles

def generate_grid(size, density):

    grid = np.zeros((size, size))

    for i in range(size):
        for j in range(size):
            if random.random() < density:
                grid[i][j] = 1  # obstacle

    return grid



# Heuristic Function (Euclidean Distance)

def heuristic(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)



# A* Path Planning Algorithm

def astar(grid, start, goal):

    # 8-direction movement
    neighbors = [
        (0,1),(1,0),(0,-1),(-1,0),
        (1,1),(1,-1),(-1,1),(-1,-1)
    ]

    closed_set = set()
    came_from = {}

    gscore = {start:0}
    fscore = {start:heuristic(start, goal)}

    open_heap = []
    heapq.heappush(open_heap,(fscore[start], start))

    nodes_explored = 0

    while open_heap:

        current = heapq.heappop(open_heap)[1]
        nodes_explored += 1

        if current == goal:

            path = []

            while current in came_from:
                path.append(current)
                current = came_from[current]

            path.append(start)
            path.reverse()

            return path, nodes_explored

        closed_set.add(current)

        for dx, dy in neighbors:

            neighbor = (current[0]+dx, current[1]+dy)

            if not (0 <= neighbor[0] < GRID_SIZE and 0 <= neighbor[1] < GRID_SIZE):
                continue

            if grid[neighbor] == 1:
                continue

            # cost for diagonal vs straight movement
            if dx != 0 and dy != 0:
                move_cost = math.sqrt(2)
            else:
                move_cost = 1

            tentative_g = gscore[current] + move_cost

            if neighbor in closed_set and tentative_g >= gscore.get(neighbor, float('inf')):
                continue

            if tentative_g < gscore.get(neighbor, float('inf')):

                came_from[neighbor] = current
                gscore[neighbor] = tentative_g
                fscore[neighbor] = tentative_g + heuristic(neighbor, goal)

                heapq.heappush(open_heap,(fscore[neighbor], neighbor))

    return None, nodes_explored



# Visualization

def visualize(grid, path, start, goal, density_level):

    plt.figure(figsize=(7,7))
    plt.imshow(grid, cmap='gray_r')

    if path:
        x = [p[1] for p in path]
        y = [p[0] for p in path]
        plt.plot(x, y, linewidth=2)

    plt.scatter(start[1], start[0], marker='o', label='Start')
    plt.scatter(goal[1], goal[0], marker='x', label='Goal')

    plt.title(f"UGV Path Planning - Density: {density_level}")
    plt.legend()
    plt.show()



# Measures of Effectiveness (MoE)

def evaluate_performance(path, nodes_explored, computation_time):

    if path:
        path_length = 0

        for i in range(len(path)-1):

            dx = abs(path[i][0] - path[i+1][0])
            dy = abs(path[i][1] - path[i+1][1])

            if dx == 1 and dy == 1:
                path_length += math.sqrt(2)
            else:
                path_length += 1

        success = True

    else:
        path_length = None
        success = False

    print("\n Measures of Effectiveness :-")
    print("Success:", success)
    print("Path Length (km):", path_length)
    print("Nodes Explored:", nodes_explored)
    print("Computation Time (seconds):", computation_time)



# Simulation Runner

def run_simulation(density_level):

   
    print("Running Simulation for Density:", density_level)

    density = DENSITY_LEVELS[density_level]

    grid = generate_grid(GRID_SIZE, density)

    start = (0,0)
    goal = (GRID_SIZE-1, GRID_SIZE-1)

    grid[start] = 0
    grid[goal] = 0

    start_time = time.time()

    path, nodes_explored = astar(grid, start, goal)

    end_time = time.time()

    computation_time = end_time - start_time

    evaluate_performance(path, nodes_explored, computation_time)

    visualize(grid, path, start, goal, density_level)



# Run Simulations for All Density Levels

if __name__ == "__main__":

    for density in ["low", "medium", "high"]:
        run_simulation(density)
