# UGV Path Planning using A* Algorithm

## Overview

This project simulates an **Unmanned Ground Vehicle (UGV)** navigating a battlefield grid while avoiding obstacles.
The objective is to find the **shortest path from a start node to a goal node** using the **A* (A-Star) algorithm**.

The battlefield is modeled as a **70 × 70 grid**, where each cell represents **1 km × 1 km**. Obstacles are randomly generated with different densities to simulate varying battlefield conditions.

---

## Features

* 70 × 70 grid battlefield representation
* Random obstacle generation
* Three obstacle density levels:

  * Low (10%)
  * Medium (20%)
  * High (35%)
* A* search algorithm for shortest path planning
* 8-direction UGV movement (including diagonals)
* Path visualization using matplotlib
* Measures of Effectiveness (MoE):

  * Path length
  * Nodes explored
  * Computation time
  * Success rate

---

## Algorithm

The system uses the **A* search algorithm** to compute the optimal path.

The evaluation function used is:

**f(n) = g(n) + h(n)**

Where:

* **g(n)** = actual cost from the start node to the current node
* **h(n)** = heuristic estimate (Euclidean distance) from the current node to the goal

This ensures the algorithm finds the **shortest valid path while avoiding obstacles**.

---

## Project Structure

```
UGV_Q2/
│
├── UGV.py
└── README.md
```

* **UGV.py** – Contains the full implementation of the UGV path planning algorithm.

---

## Requirements

Install the required Python libraries:

```
pip install numpy matplotlib
```

---

## How to Run

1. Open a terminal in the project folder.

2. Run the program:

```
python UGV.py
```

3. The simulation will run for **low, medium, and high obstacle densities** and display the computed path.

---

## Output

For each obstacle density, the program prints:

* Navigation success or failure
* Path length
* Nodes explored
* Computation time

It also displays a **visual grid showing obstacles and the optimal path from Start to Goal**.

---

## Conclusion

This project demonstrates how the **A* path planning algorithm** can be used for autonomous navigation in a grid-based battlefield environment. The approach efficiently computes the shortest path while avoiding obstacles and provides performance metrics for evaluation.

