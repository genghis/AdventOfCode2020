input_list = [x.strip() for x in open('./input.txt')]
input_list.append('')
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
		passport_list.append(input_list[previous_place:current_place])
		previous_place = current_place+1

def validate_passport(passport):
	passport_string = ' '.join(passport)
	smashport = passport_string.split(' ')
	field_list = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
	fields = {k:v for (k,v) in [x.split(':') for x in smashport]}
	try:
		matches = 0
		if len(fields['byr']) == 4 and 1920 <= int(fields['byr']) <= 2002:
			matches += 1
		if len(fields['iyr']) == 4 and 2010 <= int(fields['iyr']) <= 2020:
			matches += 1
		if len(fields['eyr']) == 4 and 2020 <= int(fields['eyr']) <= 2030:
			matches += 1
		if fields['hgt'][-2:] == "in" and 59 <= int(fields['hgt'][:-2]) <= 76:
			matches += 1
		if fields['hgt'][-2:] == "cm" and 150 <= int(fields['hgt'][:-2]) <= 193:
			matches += 1
		if fields['hcl'][0] == "#" and len(fields['hcl']) == 7 and all(x in "abcdef0123456789" for x in fields['hcl'][1:]):
			matches += 1
		if fields['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
			matches += 1
		if len(fields['pid']) == 9 and all(x in "0123456789" for x in fields['pid']):
			matches += 1
		if matches == 7:	
			return True
		else:
			return False
	except:
		return False

chopped_list(input_list)
create_passports(empty_lines)
print(len(list(filter(validate_passport, passport_list))))