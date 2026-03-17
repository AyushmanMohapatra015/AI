import numpy as np
import heapq
import random
import math
import time
import matplotlib.pyplot as plt

GRID_SIZE = 70
DYNAMIC_PROB = 0.02


def heuristic(a,b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)


def generate_grid(size,density):

    grid = np.zeros((size,size))

    for i in range(size):
        for j in range(size):

            if random.random() < density:
                grid[i][j] = 1

    return grid


def astar(grid,start,goal):

    neighbors = [
        (0,1),(1,0),(0,-1),(-1,0),
        (1,1),(1,-1),(-1,1),(-1,-1)
    ]

    open_list=[]
    heapq.heappush(open_list,(0,start))

    came_from={}
    gscore={start:0}

    nodes_explored=0

    while open_list:

        current=heapq.heappop(open_list)[1]
        nodes_explored+=1

        if current==goal:

            path=[]

            while current in came_from:
                path.append(current)
                current=came_from[current]

            path.append(start)
            path.reverse()

            return path,nodes_explored

        for dx,dy in neighbors:

            neighbor=(current[0]+dx,current[1]+dy)

            if not (0<=neighbor[0]<GRID_SIZE and 0<=neighbor[1]<GRID_SIZE):
                continue

            if grid[neighbor]==1:
                continue

            cost = math.sqrt(2) if dx!=0 and dy!=0 else 1

            tentative = gscore[current] + cost

            if tentative < gscore.get(neighbor,float('inf')):

                came_from[neighbor]=current
                gscore[neighbor]=tentative

                fscore = tentative + heuristic(neighbor,goal)

                heapq.heappush(open_list,(fscore,neighbor))

    return None,nodes_explored


def add_dynamic_obstacles(grid,start,goal,current):

    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):

            if random.random()<DYNAMIC_PROB:

                if (i,j)!=start and (i,j)!=goal and (i,j)!=current:
                    grid[i][j]=1


def simulate():

    grid=generate_grid(GRID_SIZE,0.15)

    start=(0,0)
    goal=(GRID_SIZE-1,GRID_SIZE-1)

    grid[start]=0
    grid[goal]=0

    current=start
    path_taken=[current]

    total_nodes=0
    replans=0

    start_time=time.time()

    while current!=goal:

        path,nodes=astar(grid,current,goal)
        total_nodes+=nodes

        if path is None:
            print("No path available!")
            return

        next_step=path[1]

        add_dynamic_obstacles(grid,start,goal,current)

        if grid[next_step]==1:

            replans+=1
            continue

        current=next_step
        path_taken.append(current)

    end_time=time.time()

    print("\nDynamic Navigation Results")
    print("Path Length:",len(path_taken))
    print("Nodes Explored:",total_nodes)
    print("Replans:",replans)
    print("Computation Time:",end_time-start_time)

    visualize(grid,path_taken,start,goal)


def visualize(grid,path,start,goal):

    plt.imshow(grid,cmap="gray_r")

    x=[p[1] for p in path]
    y=[p[0] for p in path]

    plt.plot(x,y,linewidth=2)

    plt.scatter(start[1],start[0],marker='o',label="Start")
    plt.scatter(goal[1],goal[0],marker='x',label="Goal")

    plt.title("UGV Dynamic Obstacle Navigation")

    plt.legend()
    plt.show()


if __name__=="__main__":
    simulate()
