total = 0
with open('lesson_5.txt', 'w+') as f:
    user_request = '#'
    while user_request != '':
        user_request = input('Введите число: ')
        f.write(user_request + ' ')
    f.seek(0)
    numbers = f.readline()
print(f'Ряд числе: {numbers}')
my_list = numbers.split(' ')
for i in my_list:
    if i != '':
        total += int(i)
print(f'Их сумма: {total}')
