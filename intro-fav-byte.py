hex = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
byte = bytes.fromhex(hex)
# byte ^ x  = x
# flag = hex ^ byte

def byte_xor(ba1, ba2):
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])

'''for i in range(len(byte)):
    flag = byte_xor(byte, byte[i])
    print(flag)'''

flag = byte_xor(byte, b"13")
print(flag)