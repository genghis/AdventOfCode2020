input_list = [x.strip() for x in open('./input.txt')]
input_list.append('')
input_list.insert(0, '')
empty_lines = []
passport_list = []
valid_passports = 0

def chopped_list(mis_en_place):
	current_line = 0
	for i in mis_en_place:
		if i == '':
			empty_lines.append(current_line)
			current_line += 1
			pass
		else:
			current_line += 1
			pass

def create_passports(empty_line_list):
	previous_place = 0
	current_place = 0
	for i in empty_line_list:
		current_place = i
		passport_list.append(input_list[previous_place+1:current_place])
		previous_place = current_place

def validate_passport(passport):
	passport_string = ' '.join(passport)
	smashport = passport_string.split(' ')
	print(smashport)
	if len(smashport) == 8:
		return True
	elif len(smashport) == 7 and "cid:" not in passport_string:
		return True
	else:
		return False

chopped_list(input_list)
create_passports(empty_lines)
print(empty_lines)
print(len(list(filter(validate_passport, passport_list))))