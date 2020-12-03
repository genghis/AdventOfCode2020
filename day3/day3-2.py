import os

input_list = [list(x.strip()) for x in open('input.txt', 'r')]
slope_list = [(1,1),(3,1),(5,1),(7,1),(1,2)]
trees_product = 1

def ski(slope):
	x_coord = 0
	y_coord = 0
	trees = 0
	while y_coord < len(input_list)-1:
		x_coord += slope[0]
		y_coord += slope[1]
		if x_coord > len(input_list[y_coord]) - 1:
			x_coord = x_coord - len(input_list[y_coord])
		if input_list[y_coord][x_coord] == "#":
			trees += 1
	return(trees)

trees_list = list(map(ski, slope_list))

for tree in trees_list:
	trees_product = trees_product * tree

print(f'Trees List is {trees_list}, multipled is {trees_product}')