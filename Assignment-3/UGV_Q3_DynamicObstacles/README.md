# UGV Dynamic Path Planning (Q2)

## Overview

This project extends the previous UGV navigation problem where all obstacles were **static and known beforehand**. In the real world, however, obstacles can be **dynamic, unpredictable, and not known a priori**. Examples include moving vehicles, soldiers, debris, or newly discovered hazards.

To address this, the UGV must **continuously monitor the environment and update its path while moving**. This project simulates such a scenario using a **dynamic path replanning approach** based on the **A* algorithm**.

The battlefield is modeled as a **70 × 70 grid**, where each grid cell represents **1 km × 1 km** of terrain.

---

## From Static to Dynamic Navigation

### Static Obstacle Environment (Previous Problem)

In the first problem:

* All obstacles were **known beforehand**
* The UGV could compute the **optimal path once using A***
* The environment **did not change during navigation**

Workflow:

1. Generate battlefield grid
2. Compute shortest path using A*
3. Follow the path until the goal is reached

---

### Dynamic Obstacle Environment (This Problem)

In real-world environments:

* Obstacles may **appear or move**
* The original path may **become blocked**
* The UGV must **recompute its path during movement**

This project implements **dynamic replanning** where:

1. The UGV computes an initial path using **A***
2. The UGV moves **step by step**
3. **New obstacles may appear randomly**
4. If the current path becomes blocked:

   * The UGV **replans a new optimal path**
5. The process continues until the **goal is reached**

This approach mimics the behavior of advanced robotics algorithms such as **D* Lite**, which are used in autonomous vehicles and planetary rovers.

---

## Features

* 70 × 70 battlefield grid
* Random initial obstacle generation
* Dynamic obstacles appearing during navigation
* A* search algorithm for optimal path planning
* 8-direction movement (including diagonals)
* Automatic path replanning when obstacles appear
* Visualization of the final navigation path
* Performance evaluation metrics

---

## Measures of Effectiveness

The following metrics are used to evaluate the performance of the UGV navigation system:

* **Path Length** – total distance traveled by the UGV
* **Nodes Explored** – number of nodes expanded during search
* **Replans** – number of times the path had to be recomputed
* **Computation Time** – total time required to reach the goal

These metrics help measure the **efficiency and robustness of the navigation algorithm in dynamic environments**.

---

## Project Structure

```id="5bxvfx"
UGV_Q2/
│
├── UGV_Dynamic.py
└── README.md
```

* **UGV_Dynamic.py** – Implementation of dynamic UGV navigation with path replanning.

---

## Requirements

Install the required Python libraries:

```id="i9ijya"
pip install numpy matplotlib
```

---

## How to Run

1. Open a terminal in the project folder.

2. Run the simulation:

```id="93cexx"
python UGV_Dynamic.py
```

3. The program will simulate the UGV navigating the battlefield while **dynamic obstacles appear**.

4. If the path becomes blocked, the system will **automatically replan a new optimal path**.

---

## Output

The program produces:

### Terminal Output

Performance metrics such as:

* path length
* nodes explored
* number of replanning events
* total computation time

### Visualization

A graphical grid showing:

* obstacles
* start position
* goal position
* path taken by the UGV

---

## Conclusion

This project demonstrates how a UGV can navigate in an environment with **dynamic and unknown obstacles**. By combining **A* search with dynamic replanning**, the UGV is able to continuously adapt to environmental changes and safely reach its destination.

Such techniques are commonly used in **robotics, autonomous vehicles, and exploration rovers** where environments are uncertain and constantly changing.

