# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

try:
    with open("my_file.txt", "w") as f_obj:
        while True:
            my_inf = input('Несколько слов: ')
            if my_inf == "":
                break
            print(my_inf, file=f_obj)

except Exception as err:
    print("Ошибка:", err)

# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

def func_count_words(str_file):
    x = str_file.split()
    l = len(x)
    return l


try:
    with open("my_file1.txt", "r") as f_obj:
        i = 0
        for str_file in f_obj:
            i += 1
            print(func_count_words(str_file))
        print(i)

except Exception as err:
    print("Ошибка:", err)

# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

try:
    with open("my_file3.txt", "r", encoding="utf-8") as f_obj:
        no_money_no_honey = 20000
        i = 0
        sum_money = 0

        for str_file in f_obj:
            empl_arr = str_file.split(':')
            name = empl_arr[0]
            money = int(empl_arr[1])
            if money < no_money_no_honey:
                print(name)
            i += 1
            sum_money += money
        med = sum_money / i
        print('Средняя зар.плата:', med)

except Exception as err:
    print("Ошибка:", err)

# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
#
my_dict = {'One': 'один', 'Two': 'два', 'Three': 'три', 'Four': 'четыре'}
new_list = []

try:
    with open("my_file4.txt", "r", encoding="utf-8") as f_obj:
        for str_file in f_obj:
            new_str = str_file.split(' - ')
            if new_str[0] in my_dict.keys():
                numeral = my_dict.get(new_str[0])
                new_list.append(numeral+' - '+new_str[1])
        print(new_list)

except Exception as err:
    print("Ошибка:", err)

with open('my_file4_1.txt', 'w', encoding="utf-8") as f_obj1:
    f_obj1.writelines(new_list)

#5 . Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
import random

n = 10
n2 = 100

with open("my_file5.txt", "w", encoding="utf-8") as f_obj:
    for i in range(n):
        f_obj.write(str(random.randint(0, n2))+" ")


sum_num = 0


with open("my_file5.txt", "r", encoding="utf-8") as f_obj:
    for str_file in f_obj:
        num_list = str_file.split()
        for num_list1 in num_list:
            sum_num += int(num_list1)

print(sum_num)

# 6 Необходимо создать (не программно) текстовый файл, где каждая строка описывает
# учебный предмет и наличие лекционных, практических и лабораторных занятий по этому
# предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все
# типы занятий. Сформировать словарь, содержащий название предмета и общее количество
# занятий по нему. Вывести словарь на экран.

my_dict = dict()
with open("my_file6.txt", "r", encoding="utf-8") as f_obj:
    for str_file in f_obj:
        str_list1 = str_file.split(":")
        name = str_list1[0]
        sum = 0
        str_list_digit = str_list1[1].split()
        for str_digit in str_list_digit:
            if str_digit != "-":
                str_digit_good = ''.join(x for x in str_digit if x.isdigit())
                sum += int(str_digit_good)

        my_dict[name] = sum

    print(my_dict)

# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь
# со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

try:
    output_list = list()
    comp_profit_dict = dict()
    avg_profit_dict = dict()
    sum_profit = 0
    num_profit = 0
    with open("company.txt", "r", encoding="utf-8") as f_obj:
        for line in f_obj:
            comp_args = line.split("   ")
            print(comp_args)

            comp_name = comp_args[0]
            comp_type = comp_args[1]
            comp_income = int(comp_args[2])
            comp_outcome = int(comp_args[3])
            comp_profit = comp_income - comp_outcome

            comp_profit_dict[comp_name] = comp_profit

            if comp_profit > 0:
                sum_profit += comp_profit
                num_profit += 1

        avg_profit = sum_profit / num_profit
        avg_profit_dict["average_profit"] = avg_profit

    output_list.append(comp_profit_dict)
    output_list.append(avg_profit_dict)

    print(output_list)
except IOError:
    print("Произошла ошибка ввода-вывода!")