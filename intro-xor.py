flagStr = "label"
flagInt = []
flagAscii = []
flag = ''
for c in flagStr:
     flagInt.append(ord(c))

for i in flagInt:
    flagAscii.append(i^13)

for c in flagAscii:
    flag = flag + chr(c)

print("crypto{%s}" % flag)