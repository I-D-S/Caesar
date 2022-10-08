# Создаём список букв
a = ord('а')
alphabet = ''.join([chr(i) for i in range(a,a+6)] + [chr(a+33)] +[chr(i) for i in range(a+6,a+32)])
# Заглавные буквы
b_alphabet = alphabet.upper()
while True:
    string = input('Введите текст кириллицей:   ')
    if string == '0':
        break
    try:
        decision = int(input('Введите 1 для шифровки -1 для расшифровки:   '))
        assert decision == 1 or decision == -1
        n = int(input('Введите шаг смещения(целое число):    '))
    except AssertionError:
        print('Неверный шаг расшифровки')
        break
    except ValueError:
        print('Шаг смещения должен быть целым числом!')
        break
    output = ''     #Строка вывода
    # Заменяем каждую букву на букву с индексом большим на шаг смещения
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
