# Задача 1.

from sys import argv

script_name, total_hours, m_hours, surprise = argv


def money(total_hours, m_hours, surprise):
    total = int(total_hours) * int(m_hours) + int(surprise)
    return total


print(money(total_hours, m_hours, surprise))

# Задача 2.

my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [my_list[el] for el in range(1, len(my_list)) if my_list[el] > my_list[el - 1]]

print(new_list)

# Задача 3.

new_list = [el for el in range(20, 240) if el % 20 == 0 or el % 21 == 0]
print(new_list)

# Задача 4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.

my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [el for el in my_list if my_list.count(el) == 1]
print(new_list)

# Задача 5.Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().
from functools import reduce

my_list = [el for el in range(100, 1001) if el % 2 == 0]


def my_func(prev_el, el):
    return prev_el * el


print(reduce(my_func, my_list))

# Задача 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from itertools import count, cycle
from sys import argv
from time import sleep

#
# # скрипт первый!

script_name = argv

for el in count(3):
    if el > 10:
        break
    else:
        print(el)
        sleep(1)

print(type(el))
#
# # скрипт второй!
#
my_list = [0, 1, 2, 3]
cucumber = 0

for el in cycle(my_list):
    if cucumber == 12:
        break
    print(el)
    cucumber += 1
    sleep(1)

# Задача 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n.
# Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

from fact import fact


def my_gen(n):
    f_num = 1
    for el1 in range(1, n + 1):
        f_num *= el1
        yield f_num


for el in my_gen(5):
    print(el)
