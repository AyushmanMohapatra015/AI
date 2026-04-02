# Cryptarithmetic Puzzle: TWO + TWO = FOUR
# CSP approach: each letter is a distinct digit (0-9) with no leading zeros

from itertools import permutations
import matplotlib.pyplot as plt

def solve_cryptarithmetic():
    solutions = []

    # Trying all the permutations of 6 distinct digits for (F, O, U, R, T, W)
    for perm in permutations(range(10), 6):
        F, O, U, R, T, W = perm

        if T == 0 or F == 0:  
            continue

        TWO  = 100*T + 10*W + O
        FOUR = 1000*F + 100*O + 10*U + R

        if 2 * TWO == FOUR:   # main arithmetic constraint
            solutions.append((F, O, U, R, T, W))

    return solutions


solutions = solve_cryptarithmetic()

print("=" * 40)
print("  Cryptarithmetic: TWO + TWO = FOUR")
print("=" * 40)
print(f"\n  Total solutions found: {len(solutions)}\n")

for i, (F, O, U, R, T, W) in enumerate(solutions, 1):
    TWO  = 100*T + 10*W + O
    FOUR = 1000*F + 100*O + 10*U + R
    print(f"  Solution {i}: F={F} O={O} U={U} R={R} T={T} W={W}")
    print(f"    {T}{W}{O} + {T}{W}{O} = {FOUR}\n")

print("=" * 40)

# Visualization
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
fig.patch.set_facecolor("#1e1e2e")

# Puzzle display
ax1 = axes[0]
ax1.set_facecolor("#1e1e2e")
ax1.set_xlim(0, 5)
ax1.set_ylim(0, 6)
ax1.axis("off")
ax1.set_title("Cryptarithmetic Puzzle", color="white", fontsize=14, pad=12)

for text, y, color in [("  T W O", 4.5, "#a6e3a1"), ("+ T W O", 3.5, "#a6e3a1"),
                        ("─────────", 2.8, "#cdd6f4"), ("F O U R", 2.0, "#89b4fa")]:
    ax1.text(2.5, y, text, color=color, fontsize=22,
             fontfamily="monospace", ha="center", va="center", fontweight="bold")

ax1.text(2.5, 0.8, "Each letter = unique digit (0–9)\nNo leading zeros: T ≠ 0, F ≠ 0",
         color="#bac2de", fontsize=10, ha="center", va="center")

# Solutions table
ax2 = axes[1]
ax2.set_facecolor("#1e1e2e")
ax2.axis("off")
ax2.set_title("Solutions Found", color="white", fontsize=14, pad=12)

col_labels = ["F", "O", "U", "R", "T", "W", "TWO", "FOUR", "✓"]
table_data = [[F, O, U, R, T, W,
               100*T+10*W+O,
               1000*F+100*O+10*U+R, "✓"] for F, O, U, R, T, W in solutions]

table = ax2.table(cellText=table_data, colLabels=col_labels, loc="center", cellLoc="center")
table.auto_set_font_size(False)
table.set_fontsize(11)
table.scale(1.2, 2.2)

for j in range(len(col_labels)):
    table[0, j].set_facecolor("#313244")
    table[0, j].set_text_props(color="#cba6f7", fontweight="bold")

for i in range(1, len(table_data) + 1):
    for j in range(len(col_labels)):
        table[i, j].set_facecolor("#181825")
        table[i, j].set_text_props(color="#a6e3a1" if j == len(col_labels)-1 else "#cdd6f4")

plt.suptitle("TWO + TWO = FOUR  |  CSP Backtracking Solution",
             color="white", fontsize=13, y=1.01)
plt.tight_layout()
plt.savefig("cryptarithmetic_solution.png", dpi=150, bbox_inches="tight", facecolor="#1e1e2e")
plt.show()
print("Saved: cryptarithmetic_solution.png")
