# Dijkstra’s Algorithm on Indian Cities

## Description

In this problem, I implemented Dijkstra’s Algorithm (also known as Uniform Cost Search) to find the shortest path between cities in India based on road distances.

Each city is treated as a node and the roads between them are treated as weighted edges, where the weight represents the distance in kilometers.

---

## Approach

* The graph is represented using an **adjacency list**
* A **priority queue (min-heap)** is used to always pick the city with the smallest distance
* The algorithm starts from a source city and updates the shortest distance to all other cities
* It also keeps track of the path using a parent dictionary

---

## Algorithm Steps

1. Initialize distance of all cities as infinity
2. Set source distance = 0
3. Push source into priority queue
4. While queue is not empty:

   * Extract the city with minimum distance
   * Update distances of its neighbors if a shorter path is found
5. Repeat until all cities are processed

---

## Output

The program gives:

* Shortest distance from source to all cities
* Shortest path from source to a given destination

---

## Concepts Used

* Graphs (Adjacency List)
* Priority Queue (Min Heap)
* Greedy Algorithm
* Uniform Cost Search

---

## How to Run the Code

1. Make sure Python is installed
2. Navigate to this folder in terminal
3. Run the program:

```bash
python dijkstra_india.py
```

4. Enter:

   * Source city
   * Destination city

5. The output will display:

   * Shortest distances
   * Optimal path

---

## Notes

* The dataset used is a small set of major Indian cities with approximate road distances
* The graph is undirected since roads are two-way
* This implementation can be extended to larger datasets or real-world maps

