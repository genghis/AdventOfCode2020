import os
import itertools

input_list = [int(x) for x in open('input.txt', 'r')]

trios = set((sorted((x,y,z))[0],sorted((x,y,z))[1],sorted((x,y,z))[2]) for x,y,z in itertools.product(input_list, input_list, input_list))

for i in trios:
	if i[0]+i[1]+i[2] == 2020:
		print(f"{i[0]} + {i[1]} + {i[2]} = 2020\n{i[0]} x {i[1]} x {i[2]}= {i[0]*i[1]*i[2]}")