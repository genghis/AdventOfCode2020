import os

input_list = [x.strip() for x in open('./input.txt')]

valid_count = 0

for i in input_list:
	ituple= i.split(' ')
	number_range = ituple[0].split('-')
	minimum = int(number_range[0])
	maximum = int(number_range[1])
	letter = ituple[1][0]
	password = ituple[2]
	total = password.count(letter)
	if total >= minimum and total <= maximum:
		valid_count += 1

print(valid_count)