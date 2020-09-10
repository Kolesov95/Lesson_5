import json
firm_dict = {}
av_dict = {}
success_count = 0
sum_income = 0
line = '#'
i = 0
with open('lesson_7.txt', 'r', encoding='utf-8') as f:
    str_quantity = len(f.readlines())
    f.seek(0)
    while i != str_quantity:
        line = f.readline().strip()
        my_list = line.split('   ')
        income = int(my_list[2]) - int(my_list[3])
        if income > 0:
            sum_income += income
            success_count += 1
        firm_dict[my_list[0]] = income
        i += 1
av_dict['average_profit'] = round(sum_income/success_count, 2)
final_list = [firm_dict, av_dict]
print(final_list)
with open('income.json', 'w', encoding='utf-8') as income_f:
    json.dump(final_list, income_f)
