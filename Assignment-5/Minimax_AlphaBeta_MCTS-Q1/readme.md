# AI Game Search Algorithms (Tic-Tac-Toe)

This project implements four classical AI game search algorithms using Tic-Tac-Toe as the test environment.

---

## Algorithms Implemented

- Minimax Search  
- Alpha-Beta Pruning  
- Heuristic Alpha-Beta Search  
- Monte-Carlo Tree Search (MCTS)  

---

## Problem

The objective is to make intelligent decisions in a two-player adversarial game using different AI search techniques.

The game used for testing is Tic-Tac-Toe.

---

## Approach

- Game Environment → Tic-Tac-Toe  
- Players → X (MAX), O (MIN)  
- State Space → Board configurations  
- Goal → Choose the optimal move  

---

## Algorithms Used

### Minimax Search

Explores the complete game tree recursively and selects the optimal move assuming perfect play from both players.

### Alpha-Beta Pruning

Optimized version of Minimax that prunes unnecessary branches and reduces computation.

### Heuristic Alpha-Beta Search

Uses:
- Depth-limited search  
- Heuristic evaluation function  
- Alpha-Beta pruning  

to improve efficiency.

### Monte-Carlo Tree Search (MCTS)

Uses:
- Random simulations  
- Exploration vs exploitation  
- UCT formula  

to select moves probabilistically.

---

## Heuristic Function

The heuristic evaluation function:

- Rewards winning opportunities  
- Penalizes opponent threats  
- Evaluates non-terminal board states  

---

## Test Cases

The implementation includes tests for:

- Winning move detection  
- Blocking opponent moves  
- Terminal state detection  
- Draw detection  
- Cross-algorithm validation  
- Performance comparison  

---

## Performance Observation

- Alpha-Beta explores fewer nodes than Minimax  
- Heuristic Alpha-Beta is the fastest algorithm  
- MCTS performs randomized search efficiently  

---

## Example Result

```text
RESULTS: 28/30 tests passed
```

Note:

Monte-Carlo Tree Search is probabilistic and may occasionally produce non-optimal moves because of randomized simulations.

---

## How to Run

Make sure Python is installed, then run:

```bash
python game_search_algorithms.py
```

---

## Technologies Used

- Python  
- Object-Oriented Programming  
- Heuristic Evaluation  
- Monte-Carlo Simulation  

---

## AI Concepts Demonstrated

- Adversarial Search  
- Game Trees  
- Decision Making  
- Heuristic Search  
- Search Optimization  
- Monte-Carlo Simulation  

---

## Conclusion

This project successfully demonstrates the implementation and comparison of Minimax, Alpha-Beta, Heuristic Alpha-Beta, and Monte-Carlo Tree Search algorithms for intelligent decision-making in adversarial games.
