
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import networkx as nx

adjacency = {
    "Adilabad":               ["Kumurambheem Asifabad", "Nirmal", "Mancherial"],
    "Kumurambheem Asifabad":  ["Adilabad", "Mancherial"],
    "Nirmal":                 ["Adilabad", "Nizamabad", "Kamareddy", "Mancherial", "Jagtial"],
    "Mancherial":             ["Adilabad", "Kumurambheem Asifabad", "Nirmal", "Jagtial", "Peddapalli"],
    "Nizamabad":              ["Nirmal", "Kamareddy", "Jagtial"],
    "Jagtial":                ["Nirmal", "Mancherial", "Peddapalli", "Rajanna Sircilla", "Karimnagar", "Nizamabad"],
    "Kamareddy":              ["Nizamabad", "Nirmal", "Medak", "Sangareddy", "Rajanna Sircilla"],
    "Peddapalli":             ["Mancherial", "Jagtial", "Karimnagar", "Jayashankar Bhupalpally", "Mulugu"],
    "Rajanna Sircilla":       ["Jagtial", "Karimnagar", "Kamareddy"],
    "Karimnagar":             ["Jagtial", "Peddapalli", "Rajanna Sircilla", "Siddipet", "Jayashankar Bhupalpally"],
    "Jayashankar Bhupalpally":["Peddapalli", "Karimnagar", "Mulugu", "Warangal Urban", "Jangaon"],
    "Mulugu":                 ["Peddapalli", "Jayashankar Bhupalpally", "Bhadradri Kothagudem"],
    "Medak":                  ["Kamareddy", "Sangareddy", "Siddipet"],
    "Siddipet":               ["Medak", "Karimnagar", "Sangareddy", "Medchal-Malkajgiri", "Yadadri Bhuvanagiri", "Jangaon"],
    "Sangareddy":             ["Kamareddy", "Medak", "Siddipet", "Medchal-Malkajgiri", "Hyderabad"],
    "Jangaon":                ["Siddipet", "Jayashankar Bhupalpally", "Warangal Urban", "Yadadri Bhuvanagiri"],
    "Warangal Urban":         ["Jayashankar Bhupalpally", "Jangaon", "Warangal Rural", "Mahabubabad"],
    "Warangal Rural":         ["Warangal Urban", "Mahabubabad", "Jangaon"],
    "Mahabubabad":            ["Warangal Urban", "Warangal Rural", "Bhadradri Kothagudem", "Khammam", "Suryapet"],
    "Bhadradri Kothagudem":   ["Mulugu", "Mahabubabad", "Khammam"],
    "Khammam":                ["Bhadradri Kothagudem", "Mahabubabad", "Suryapet"],
    "Suryapet":               ["Mahabubabad", "Khammam", "Nalgonda", "Yadadri Bhuvanagiri"],
    "Medchal-Malkajgiri":     ["Sangareddy", "Siddipet", "Hyderabad", "Rangareddy", "Yadadri Bhuvanagiri"],
    "Hyderabad":              ["Sangareddy", "Medchal-Malkajgiri", "Rangareddy"],
    "Yadadri Bhuvanagiri":    ["Siddipet", "Jangaon", "Medchal-Malkajgiri", "Suryapet", "Nalgonda"],
    "Rangareddy":             ["Hyderabad", "Medchal-Malkajgiri", "Vikarabad", "Mahabubnagar", "Nalgonda"],
    "Nalgonda":               ["Yadadri Bhuvanagiri", "Suryapet", "Rangareddy", "Mahabubnagar"],
    "Vikarabad":              ["Rangareddy", "Mahabubnagar", "Sangareddy"],
    "Mahabubnagar":           ["Rangareddy", "Vikarabad", "Nalgonda", "Nagarkurnool", "Wanaparthy"],
    "Wanaparthy":             ["Mahabubnagar", "Nagarkurnool", "Gadwal"],
    "Nagarkurnool":           ["Mahabubnagar", "Wanaparthy", "Gadwal"],
    "Gadwal":                 ["Nagarkurnool", "Wanaparthy", "Jogulamba"],
    "Jogulamba":              ["Gadwal"],
}

# CSP Algorithm 

COLORS = ["red", "green", "blue", "yellow"]

def is_valid(district, color, assignment):
    """Check if assigning 'color' to 'district' violates any constraint."""
    for neighbor in adjacency[district]:
        if assignment.get(neighbor) == color:
            return False
    return True

def backtrack(districts, assignment):
    """Recursive backtracking to solve the map coloring CSP."""
    if len(assignment) == len(districts):
        return assignment  # All districts  are colored successfully

    unassigned = [d for d in districts if d not in assignment]
    district = unassigned[0]

    for color in COLORS:
        if is_valid(district, color, assignment):
            assignment[district] = color
            result = backtrack(districts, assignment)
            if result:
                return result
            del assignment[district]  # Backtracking part

    return None  


districts = list(adjacency.keys())
solution = backtrack(districts, {})

if solution:
    print("Map Coloring Solution Found!\n")
    for district, color in solution.items():
        print(f"  {district:<35} -> {color}")
    print(f"\nTotal colors used: {len(set(solution.values()))}")
else:
    print("No solution found.")


# 4. Visualization using NetworkX graph

G = nx.Graph()
G.add_nodes_from(districts)
for district, neighbors in adjacency.items():
    for neighbor in neighbors:
        G.add_edge(district, neighbor)

node_colors = [solution[d] for d in G.nodes()]

plt.figure(figsize=(18, 14))
pos = nx.spring_layout(G, seed=42, k=2.5)

nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=1200, alpha=0.9)
nx.draw_networkx_edges(G, pos, edge_color="gray", width=1.2, alpha=0.6)
nx.draw_networkx_labels(G, pos, font_size=6.5, font_weight="bold")

# Legend
legend_patches = [mpatches.Patch(color=c, label=c.capitalize()) for c in COLORS]
plt.legend(handles=legend_patches, loc="upper left", fontsize=12, title="Colors")

plt.title("Map Coloring Problem – 33 Districts of Telangana\n(CSP with Backtracking)", fontsize=16)
plt.axis("off")
plt.tight_layout()
plt.savefig("telangana_map_coloring.png", dpi=150, bbox_inches="tight")
plt.show()
print("\nGraph saved as 'telangana_map_coloring.png'")
