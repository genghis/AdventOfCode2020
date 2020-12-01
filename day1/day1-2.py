import os
import itertools

input_list = [int(x) for x in open('input.txt', 'r')]

trios = set((x,y,z) for x,y,z in itertools.combinations(input_list, 3))

def check_2020(trio):
	if sum(trio) == 2020:
		return True
	else:
		return False

solution = list(filter(check_2020, trios))[0]
print(f"{solution[0]} + {solution[1]} + {solution[2]} = 2020\n{solution[0]} x {solution[1]} x {solution[2]}= {solution[0]*solution[1]*solution[2]}")
