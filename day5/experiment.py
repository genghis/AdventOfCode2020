print(max([(int(x.strip().translate(x.maketrans("BFRL","1010")),2)) for x in open('./input.txt')]))