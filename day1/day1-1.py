import os
import itertools

input_list = [int(x) for x in open('input.txt', 'r')]

pairs = set((x,y) for x,y in itertools.combinations(input_list, 2))

for i in pairs:
	if i[0]+i[1] == 2020:
		print(f"{i[0]} + {i[1]} = 2020\n{i[0]} x {i[1]} = {i[0]*i[1]}")