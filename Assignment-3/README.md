
# Assignment 3 – Search Algorithms

## Q1: Dijkstra’s Algorithm (Uniform Cost Search)

In this question, I implemented Dijkstra’s Algorithm to find the shortest path between cities in India based on road distances.

I represented cities as nodes and roads as weighted edges. Using a priority queue, the algorithm finds the minimum cost path from a source city to all other cities. It also prints the shortest path to a given destination.

---

## Q2: UGV Navigation with Static Obstacles

Here, I worked on a problem where an Unmanned Ground Vehicle (UGV) needs to move in a grid (like a battlefield area) with obstacles that are already known.

The idea was to treat the grid as a graph and avoid blocked cells while finding the shortest path from start to goal. The obstacle density can vary, making the problem more interesting.

To evaluate the solution, I considered:

* Distance of the path
* Whether the goal is reached successfully
* Efficiency of the algorithm

---

## Q3: UGV Navigation with Dynamic Obstacles

In this part, the problem becomes more realistic because obstacles are not fixed and can change while the vehicle is moving.

Since the environment is not fully known, the algorithm needs to adjust its path whenever a new obstacle appears. So instead of computing the path just once, it may need to recompute it during movement.

Some approaches that can be used here include:

* Replanning using A*
* Dynamic algorithms like D*
* Real-time decision making
