A = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
AxB = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
BxC = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
flagxAxCxB = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"
B = ""
C = ""
flagxAxB = ""
flagxA = ""
flag = ""

def byte_xor(ba1, ba2):
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])

A = bytes.fromhex(A)
AxB = bytes.fromhex(AxB)
BxC = bytes.fromhex(BxC)
flagxAxCxB = bytes.fromhex(flagxAxCxB)
B = byte_xor(A, AxB)
C = byte_xor(B, BxC)
flagxAxB = byte_xor(flagxAxCxB, C)
flagxA = byte_xor(flagxAxB, B)
flag = byte_xor(flagxA, A)
print(flag)