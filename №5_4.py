my_list = []
line = '#'
f_new = open('lesson_new_4.txt', 'w', encoding='utf-8')
f_new.close()
with open('lesson_4.txt', 'r', encoding='utf-8') as f:
    while True:
        if line == '':
            break
        else:
            line = (f.readline()).strip()
            new_line = line.split(' — ')
            if new_line[0] == 'One':
                f_new = open('lesson_new_4.txt', 'a', encoding='utf-8')
                f_new.write(f'Один - {new_line[1]}\n')
            if new_line[0] == 'Two':
                f_new = open('lesson_new_4.txt', 'a', encoding='utf-8')
                f_new.write(f'Два - {new_line[1]}\n')
            if new_line[0] == 'Three':
                f_new = open('lesson_new_4.txt', 'a', encoding='utf-8')
                f_new.write(f'Три - {new_line[1]}\n')
            if new_line[0] == 'Four':
                f_new = open('lesson_new_4.txt', 'a', encoding='utf-8')
                f_new.write(f'Четыре - {new_line[1]}\n')
