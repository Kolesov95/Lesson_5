my_dict = {}
total = 0
line = '#'
with open('lesson_6.txt', 'r', encoding='utf-8') as f:
    while line != '':
        total = 0
        line = f.readline().strip()
        my_list = line.split()
        for i in my_list:
            if '(' in i:
                i_el = i.split('(')
                total += int(i_el[0])
            my_dict[my_list[0][:-1]] = total
print(my_dict)
