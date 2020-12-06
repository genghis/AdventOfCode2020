input_list = [x.strip() for x in open('./input.txt')]
input_list.append('')
empty_lines = []
group_answer_list = []
list_of_sets = []
total = 0

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

def create_groups(empty_line_list):
	previous_place = 0
	current_place = 0
	for i in empty_line_list:
		global total
		current_place = i
		temp_list = input_list[previous_place:current_place]
		group_answers = [x for x in str(temp_list) if x in "abcdefghijklmnopqrstuvwxyz"]
		group_dict = {x:group_answers.count(x) for x in group_answers}
		everyone_answered = len(list(filter(lambda x: x == len(temp_list), group_dict.values())))
		total += everyone_answered
		previous_place = current_place+1

chopped_list(input_list)
create_groups(empty_lines)
print(total)
