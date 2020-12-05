letter_trans = "BFRL"
binary_trans = "1010"
input_list = [x.strip().translate(x.maketrans(letter_trans,binary_trans)) for x in open('./input.txt')]

def mathing(seat):
	row = int(seat[:7],2)
	column = int(seat[7:],2)
	return (row*8)+column

largest = max(list(filter(mathing,input_list)))
l_row = int(largest[:7],2)
l_column = int(largest[7:],2)
print(f'Largest number is {(l_row*8)+l_column}')