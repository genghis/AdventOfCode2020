input_list = [(int(x.strip().translate(x.maketrans("BFRL","1010")),2)) for x in open('./input.txt')]
print(sorted(set(range(input_list[0],input_list[-1])).difference(input_list))[0])