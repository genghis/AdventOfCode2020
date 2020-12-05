letter_trans = "BFRL"
binary_trans = "1010"
input_list = [(int(x.strip().translate(x.maketrans(letter_trans,binary_trans)),2)) for x in open('./input.txt')]

def find_my_seat(pair):
	try:
		next_seat = seat_numbers[pair[0]+1][1]
		current_seat = pair[1]
		if current_seat - next_seat == 2:
			return True
		else:
			return False
	except:
		return False

seat_numbers = list(enumerate(sorted(input_list, reverse=True)))

#The my_seat math is because I am an idiot and tried to use the number that gave a True in find_my_seat, instead of the missing number
my_seat = list(filter(find_my_seat, seat_numbers))[0][1]-1

print(my_seat)