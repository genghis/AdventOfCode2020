import os
import itertools

input_list = [int(x) for x in open('input.txt', 'r')]

trios = set((x,y,z) for x,y,z in itertools.combinations(input_list, 3))

solution = list(filter(lambda x: sum(x) == 2020, trios))[0]

print(f"{solution[0]} + {solution[1]} + {solution[2]} = 2020\n{solution[0]} x {solution[1]} x {solution[2]}= {solution[0]*solution[1]*solution[2]}")
