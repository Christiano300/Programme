from tqdm import tqdm
from z3.z3 import IntVector, Solver, Distinct

pieces = IntVector('p', 26)

COLOR_MAP = {
    0: "red",
    1: "orange",
    2: "yellow",
    3: "green",
    4: "lightblue",
    5: "darkblue",
    6: "pink",
    7: "black",
    8: "white"
}

SIDES = [[0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 9, 10, 11, 17, 18, 19], [6, 7, 8, 14, 15, 16, 23, 24, 25], [17, 18, 19, 20, 21, 22, 23, 24, 25], [0, 3, 6, 9, 12, 14, 17, 20, 23], [2, 5, 8, 11, 13, 16, 19, 22, 25]]

CENTERS = {
    4: 2, # top yellow
    10: 4, # back lightblue
    12: 8, # left white
    13: 7, # right black
    15: 5, # front darkblue
    21: 1, # bottom orange
}

EDGES = [1, 3, 5, 7, 9, 11, 14, 16, 18, 20, 22, 24]
CORNERS = list(set(range(26)) - set(EDGES) - set(CENTERS.keys()))


solver = Solver()
for i in range(26):
    solver.add(pieces[i] >= 0, pieces[i] <= 8)

for pos, color in CENTERS.items():
    solver.add(pieces[pos] == color)

for side in SIDES:
    solver.add(Distinct(*[pieces[i] for i in side]))
    
for edge in EDGES:
    solver.add(pieces[edge] != 3) # edges cannot be green

for corner in CORNERS:
    # corners cannot be red or pink
    solver.add(pieces[corner] != 0)
    solver.add(pieces[corner] != 6)

solutions = [solution for solution in tqdm(solver.solutions(pieces))]
print("\n".join(str(s) for s in solutions))