my_list = []
while True:
    line = input('Введите строки: ')
    if line == '':
        break
    else:
        my_list.append(line + '\n')
f = open('lesson_1.txt', 'w', encoding='utf-8')
f.writelines(my_list)
f.close()

with open('lesson_1.txt', 'r', encoding='utf-8') as f:
    lines = f.read()
    print(lines)


