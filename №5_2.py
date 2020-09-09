line = '#'
i = 0
with open('lesson_2.txt', 'r', encoding='utf-8') as f:
    str_quantity = len(f.readlines())
    print(f'Всего строк: {str_quantity}')
    f.seek(0)
    while i != str_quantity:
        line = f.readline()
        print(f'Количество слов в строке {i+1}: {len(line.split())}')
        i += 1
