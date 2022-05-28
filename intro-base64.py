import base64
flag1 = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
flag2 = bytes.fromhex(flag1)
flag3 = base64.b64encode(flag2)

print(flag3)