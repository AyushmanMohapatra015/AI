# Map Coloring using CSP (Australia)

This project solves the Map Coloring problem for Australia using a Constraint Satisfaction Problem (CSP) approach with backtracking.

---

##  Problem

Assign colors to the regions:

`WA, NT, Q, SA, NSW, V, T`

such that no adjacent regions share the same color.

---

##  Approach

- Variables → Regions  
- Domains → Red, Green, Blue  
- Constraints → Neighboring regions must have different colors  
- Algorithm → Backtracking Search  

---

##  How to Run

Make sure Python is installed, then run:

```bash
python3 filename.py
