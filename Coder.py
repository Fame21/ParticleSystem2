n = 5

def encode(str):
    '''
    Шифрует строку сдвигом символов на n
    :param str: Строка для шифрования
    :return: Строка после шифрования
    '''
    alph = 36;
    a = ord('a')
    newStr = ''
    for char in str:
        newStr += chr((ord(char) - a + n) % alph + a)
    return newStr

def decode(str):
    '''
    ДеШифрует строку сдвигом символов на -n
    :param str: Зашифрованная сдвигом на n символов строка
    :return: Дешфированная строка
    '''
    alph = 36;
    a = ord('a')
    newStr = ''
    b = alph - n
    for char in str:
        newStr += chr((ord(char) - a + b) % alph + a)
    return newStr
    pass
