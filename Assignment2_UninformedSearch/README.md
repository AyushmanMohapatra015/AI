# Assignment 2: Uninformed Search Implementation

## BFS, DFS and Their Variants
### Problem: Missionaries and Cannibals

---

## 1. Introduction

Uninformed search (also known as blind search) is a search strategy that explores the state space without using any additional heuristic information. These algorithms only use the problem definition to find a solution.

In this assignment, the following uninformed search strategies are implemented:

- Breadth First Search (BFS)
- Depth First Search (DFS)
- Depth Limited Search (DLS)
- Iterative Deepening Depth First Search (IDDFS)

These algorithms are applied to solve the Missionaries and Cannibals problem.

---

## 2. Problem Description

Three missionaries and three cannibals are on the left bank of a river. They need to cross the river using a boat that can carry at most two people at a time.

### Constraints:

1. The boat can carry one or two people.
2. Cannibals must never outnumber missionaries on either bank (unless missionaries are zero).
3. The goal is to move all six people safely to the right bank.

---

## 3. State Representation

Each state is represented as:

(Missionaries_left, Cannibals_left, Boat_position)

Where:
- Missionaries_left = number of missionaries on left bank
- Cannibals_left = number of cannibals on left bank
- Boat_position = 1 (boat on left bank), 0 (boat on right bank)

Initial State:
(3, 3, 1)

Goal State:
(0, 0, 0)

---

## 4. Algorithms Implemented

### 4.1 Breadth First Search (BFS)

- Explores the search tree level by level.
- Uses a Queue (FIFO).
- Complete and Optimal.
- Time Complexity: O(b^d)
- Space Complexity: O(b^d)

BFS guarantees the shortest path but uses more memory.

---

### 4.2 Depth First Search (DFS)

- Explores as deep as possible before backtracking.
- Uses a Stack (LIFO).
- Not guaranteed optimal.
- Time Complexity: O(b^m)
- Space Complexity: O(bm)

DFS uses less memory but may not return the shortest solution.

---

### 4.3 Depth Limited Search (DLS)

- DFS with a fixed depth limit.
- Prevents infinite search.
- May fail if limit is too small.
- Not guaranteed optimal.

---

### 4.4 Iterative Deepening DFS (IDDFS)

- Repeatedly applies DLS with increasing depth.
- Complete and Optimal.
- Combines advantages of BFS and DFS.
- Lower memory usage than BFS.

---

## 5. Performance Comparison

The algorithms were compared based on:

- Solution Path
- Nodes Expanded
- Time Taken

### Observations:

- BFS finds the shortest solution.
- DFS may find a longer solution.
- IDDFS also finds the optimal solution.
- BFS uses more memory.
- DFS uses less memory.
- Execution time is very small due to small state space.

---

## 6. Conclusion

The Missionaries and Cannibals problem was successfully solved using BFS, DFS, DLS, and IDDFS.

BFS guarantees optimality but uses more memory.  
DFS is memory efficient but not optimal.  
IDDFS provides a balanced and efficient uninformed search strategy.

---

## 7. How to Run the Code

```bash
python missionaries_cannibals.py
