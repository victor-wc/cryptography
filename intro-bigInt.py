import Crypto.Util.number

flagDec = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
flagHex = Crypto.Util.number.long_to_bytes(flagDec)

print(flagHex)