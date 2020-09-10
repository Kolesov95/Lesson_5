small_salary = []
sum_salary = 0
n = 0
with open('lesson_3.txt', 'r', encoding='utf-8') as f:
    str_quantity = len(f.readlines())
    f.seek(0)
    while n != str_quantity:
        line = (f.readline()).strip()
        my_list = line.split(': ')
        sum_salary = sum_salary + int(my_list[1])
        if int(my_list[1]) < 20000:
            small_salary.append(my_list[0])
        n += 1
print(f'Средняя зарплата: {sum_salary/str_quantity}')
print('Сотрудники с зарплатой менее 20000: ')
for i in small_salary:
    print(i)
