import os

input_list = [x.strip().replace(':','').split(' ') for x in open('./input.txt')]

def check(payload):
	numbers = payload[0].split('-')
	minimum,maximum,letter,password = int(numbers[0]), int(numbers[1]),payload[1],payload[2]
	if password.count(letter) >= minimum and password.count(letter) <= maximum:
		return True
	else:
		return False

print(len(list(filter(check,input_list))))