import os

input_list = [list(x.strip()) for x in open('input.txt', 'r')]

x_coord = 0
y_coord = 0
trees = 0

while y_coord < len(input_list)-1:
	x_coord += 3
	y_coord += 1
	if x_coord > len(input_list[y_coord]) - 1:
		x_coord = x_coord - len(input_list[y_coord])
	if input_list[y_coord][x_coord] == "#":
		trees += 1

print(trees)