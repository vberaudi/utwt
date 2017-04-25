import pandas as pd
import pandas as pd

from docplex.cp.model import *

GRNG = range(9)
problem_data = pd.read_csv("sudoku.csv", sep=";")
problem = []
for t in problem_data.itertuples(index=False):
    problem.append([i for i in t])
    
mdl = CpoModel(name="Sudoku")
grid = [[integer_var(min=1, max=9, name="C" + str(l) + str(c)) for l in GRNG] for c in GRNG]
for l in GRNG:
    mdl.add(all_diff([grid[l][c] for c in GRNG]))

for c in GRNG:
    mdl.add(all_diff([grid[l][c] for l in GRNG]))

ssrng = range(0, 9, 3)
for sl in ssrng:
    for sc in ssrng:
        mdl.add(all_diff([grid[l][c] for l in range(sl, sl + 3) for c in range(sc, sc + 3)]))
for l in GRNG:
    for c in GRNG:
        v = problem[l][c]
        if v > 0:
            print(l)
            print(c)
            print(v)
            print("...")
            grid[l][c].set_domain((v, v))
            
print("\nSolving model....")
msol = mdl.solve(TimeLimit=10)

sol = [[msol[grid[l][c]] for c in GRNG] for l in GRNG]
pd.DataFrame(sol).to_csv("sudoku_res.csv")
from docplex.worker.clientapi import set_output_attachments
outputs = dict()
outputs['sudoku_res.csv'] = './sudoku_res.csv'

set_output_attachments(outputs)
