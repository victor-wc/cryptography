flag1 = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
flag2 = ''
for character in flag1:
	flag2 = flag2 + chr(character)

print(flag2)