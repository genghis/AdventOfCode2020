letter_trans = "BFRL"
binary_trans = "1010"
input_list = [x.strip().translate(x.maketrans(letter_trans,binary_trans)) for x in open('./input.txt')]

def mathing(seat):
	row = int(seat[:7],2)
	column = int(seat[7:],2)
	return (row*8)+column

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

seat_numbers = list(enumerate(sorted([x for x in map(mathing, input_list)], reverse=True)))

my_seat = list(filter(find_my_seat, seat_numbers))[0][1]-1

print(my_seat)