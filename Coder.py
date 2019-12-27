n = 5

def encode(str):
    alph = 36;
    a = ord('a')
    newStr = ''
    for char in str:
        newStr += chr((ord(char) - a + n) % alph + a)
    return newStr

def decode(str):
    alph = 36;
    a = ord('a')
    newStr = ''
    b = alph - n
    for char in str:
        newStr += chr((ord(char) - a + b) % alph + a)
    return newStr
    pass
