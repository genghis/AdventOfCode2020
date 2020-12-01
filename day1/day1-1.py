import os
import itertools

input_list = [int(x) for x in open('input.txt', 'r')]

pairs = set((x,y) for x,y in itertools.combinations(input_list, 2))

def check_2020(pair):
	if sum(pair) == 2020:
		return True
	else:
		return False

solution = list(filter(check_2020, pairs))[0]

print(f"{solution[0]} + {solution[1]} = 2020\n{solution[0]} x {solution[1]} = {solution[0]*solution[1]}")