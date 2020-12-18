# Задача1 Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def s_calc():
    try:
        arg_1 = float(input("Укажите делимое: "))
        arg_2 = float(input("укажите делитель: "))
        result = arg_1 / arg_2
    except ZeroDivisionError:
        return
    return result


print(s_calc())

# Задача2  Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user_info(name, surname, year, city, email, phone):
    print(f"Здравствуйте, {name} {surname}! Теперь мы знаем, что Вы родились в {year} году, проживаете в {city}. "
          f"Мы можем написать Вам на адрес: {email} или позвонить по номеру: {phone}")


user_info(name=input('Ваше имя: '),
          surname=input('Ваша фамилия:'),
          year=input('Ваш год рождения:'),
          city=input('Ваш город проживания:'),
          email=input('Укажите свой адрес эл.почты:'),
          phone=input('Ваш телефон:'))


# Задача 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    my_list = [a, b, c]
    my_list.remove(min(a, b, c))
    my_sum = sum(my_list)
    return my_sum


print(my_func(34, 36, 3))

# Задача 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

# 1-ый способ

def my_func(x, y):
    return x ** y

print(my_func(3, -5))

# 2-ой способ
#
def my_func(x, y):
    b = 0
    k = 1
    while b > y:
        k = k * x
        b = b - 1

    return 1 / k


print(my_func(3, -5))

# Задача 5.

def get_not_int_index(my_arg_list):
    arg_len = len(my_arg_list)
    for i in range(arg_len):
        try:
            int(my_arg_list[i])
        except ValueError:
            return i
    return arg_len


sum_arg = 0

while True:
    arg = input('Укажите ряд чисел: ')
    arg_list = arg.split()
    not_int_index = get_not_int_index(arg_list)
    int_args = [int(x) for x in arg_list[:not_int_index]]
    sum_arg += sum(int_args)
    print(sum_arg)
    if not_int_index != len(arg_list):
        break
#
# # Задача 6.
# #
def int_func(var_1):
    return var_1.capitalize()


input_text = input("Введите строку:")
print(" ".join([int_func(x) for x in input_text.split()]))
