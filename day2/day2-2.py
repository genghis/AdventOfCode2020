import os

input_list = [x.strip().replace(':','').split(' ') for x in open('./input.txt')]

valid_count = 0

def check(payload):
	matches = 0
	numbers = payload[0].split('-')
	first,second,letter,password = int(numbers[0])-1, int(numbers[1])-1,payload[1],payload[2]
	if password[first] == letter:
		matches += 1
	if password[second] == letter:
		matches += 1
	if matches == 1:
		return True
	else:
		return False

print(len(list(filter(check, input_list))))