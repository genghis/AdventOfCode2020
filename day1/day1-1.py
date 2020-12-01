import os
import itertools

input_list = [int(x) for x in open('input.txt', 'r')]

pairs = set((x,y) for x,y in itertools.combinations(input_list, 2))

solution = list(filter(lambda x: sum(x) == 2020, pairs))[0]

print(f"{solution[0]} + {solution[1]} = 2020\n{solution[0]} x {solution[1]} = {solution[0]*solution[1]}")