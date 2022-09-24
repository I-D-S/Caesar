a = ord('а')
alphabet = ''.join([chr(i) for i in range(a,a+6)] + [chr(a+33)] +[chr(i) for i in range(a+6,a+32)])
b_alphabet = alphabet.upper()
while True:
    string = input()
    if string == '0':
        break
    decision = int(input('Введите 1 для шифровки -1 для расшифровки:   '))
    n = int(input('Введите шаг смещения:    '))
    output = ''
    for i in range(len(string)):
        try:
            index = alphabet.index(string[i])
            output += alphabet[(index+n*decision)%33]
        except ValueError:
                try:
                    index = b_alphabet.index(string[i])
                    output += b_alphabet[(index+n*decision)%33]
                except ValueError:
                    output += string[i]
    print(output)
