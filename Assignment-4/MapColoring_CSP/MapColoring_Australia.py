variables = ["WA", "NT", "Q", "SA", "NSW", "V", "T"]
domains = {v: ["Red", "Green", "Blue"] for v in variables}

neighbors = {
    "WA": ["NT", "SA"],
    "NT": ["WA", "SA", "Q"],
    "Q": ["NT", "SA", "NSW"],
    "SA": ["WA", "NT", "Q", "NSW", "V"],
    "NSW": ["Q", "SA", "V"],
    "V": ["SA", "NSW"],
    "T": []
}

def is_consistent(var, value, assignment):
    return all(assignment.get(n) != value for n in neighbors[var])

def select_unassigned_variable(assignment):
    for v in variables:
        if v not in assignment:
            return v

def backtrack(assignment):
    if len(assignment) == len(variables):
        return assignment

    var = select_unassigned_variable(assignment)

    for value in domains[var]:
        if is_consistent(var, value, assignment):
            assignment[var] = value
            result = backtrack(assignment)
            if result:
                return result
            del assignment[var]

    return None

solution = backtrack({})

for v in variables:
    print(v, "->", solution[v])
