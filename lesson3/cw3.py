# def my_sum(arg_1, arg_2):
#     return arg_1 + arg_2
#
# print(my_sum(20, 30))
# print(my_sum("abra", "kadabra"))
# print(my_sum(2, 3))

#Пример 2
# def ext_func(var_1):
#     def int_func(var_2):
#         return var_1 + var_2
#     return int_func
#
# f_obj = ext_func(200) # f_obj - функция
# print(f_obj(300))
# print(f_obj(250))

# Пример 3.


# def s_calc():
#     r_val = float(input("Укажите радиус: "))
#     h_val = float(input("Укажите высоту: "))
#     # площадь боковой поверхности цилиндра:
#     s_side = 2 * 3.14 * r_val * h_val
#     # площадь одного основания цилиндра:
#     s_circle = 3.14 * r_val ** 2
#     # полная площадь цилиндра:
#     s_full = s_side + 2 * s_circle
#     return s_full
#
# s_val = s_calc()
# print(s_val)

#Пример 4. (при возможной ошибке)
#
# def s_calc():
#     try:
#         r_val = float(input("Укажите радиус: "))
#         h_val = float(input("Укажите высоту: "))
#     except ValueError:
#         return
#     s_side = 2 * 3.14 * r_val * h_val
#     s_circle = 3.14 * r_val ** 2
#     s_full = s_side + 2 * s_circle
#     return s_full
#
# print(s_calc())

# Пример5. (возвращение через оператор несколько объектов)

# def s_calc():
#     try:
#         r_val = float(input("Укажите радиус: "))
#         h_val = float(input("Укажите высоту: "))
#     except ValueError:
#         return
#     s_side = 2 * 3.14 * r_val * h_val
#     s_circle = 3.14 * r_val ** 2
#     s_full = s_side + 2 * s_circle
#     return s_side, s_full
#
# s_side_val, s_full_val = s_calc()
# print(f"Площадь боковой пов-ти - {s_side_val}; Полная площадь - {s_full_val}")

# Пример6.

# позиционные параметры
# def first_func(var_1, var_2, var_3):
#     return var_1 + var_2 + var_3
#
# print(first_func(10, 20, 30))
#
# # именованные параметры
# def second_func(var_2, var_1, var_3):
#     print(f"var_2 - {var_2}; var_1 - {var_1}; var_3 - {var_3}")
#
# second_func(var_1=10, var_2=20, var_3=30)

# обязательные параметры
# def first_func(var_1, var_2, var_3):
#     return var_1 + var_2 + var_3
#
# print(first_func(10, 20, 30))
#
# # var_2 и var_3 - необязательные параметры
# def second_func(var_1, var_2=20, var_3=30):
#     return var_1 + var_2 + var_3
#
# print(second_func(10))

# Пример7.
#неопределенное число позиционных параметров
#
# def my_func(*args):
#     return args
#
# print(my_func(10, "text_1", 20, "text_2"))
#
# # неопределенное число именованных параметров
#
# def my_func(**kwargs):
#     return kwargs
#
# print(my_func(el_1=10, el_2=20, el_3="text"))

# Пример8.

# my_func = lambda p_1, p_2: p_1 + p_2
#
# print(my_func(2, 5))
# print(my_func("abra", "kadabra"))
#
# print((lambda p_1, p_2: p_1 + p_2)(2, 5))
# print((lambda p_1, p_2: p_1 + p_2)("abra", "kadabra"))
#
# new_func = lambda *args: args
# print(new_func(10, 20, 30, 40))

# Пример9.

# def named_func(param):
#     return param ** 0.5
# print(named_func(100))
#
# square_rt = lambda param: param ** 0.5
# print(square_rt(100))

# Пример10.

# print(ord("g"))
# print(chr(103))
# print(len("abracadabra"))

# abs()
# print(abs(2))
# print(abs(-2))
#
# print('--------')
#
# # round()
# print(round(2.6743))
# print(round(-2.678))
# print(round(2.6743, 3))
# print(round(-2.678, 2))

# print('--------')

# divmod()
# print(divmod(4, 2))
# print(divmod(5, 2))
# print('--------')
#
# # pow()
#
# print(pow(2, 4))
# print('--------')
#
# # max()
# iter_obj = [20, 2, 5, 100]
# print(max(iter_obj))
# iter_obj = (20, 2, 5, 100)
# print(max(iter_obj))
# iter_obj = "abrakadabra"
# print(max(iter_obj))

# print('--------')
#
# # min()
# iter_obj = [20, 2, 5, 100]
# print(min(iter_obj))
# iter_obj = (20, 2, 5, 100)
# print(min(iter_obj))
# iter_obj = "abrakadabra"
# print(min(iter_obj))
# print('--------')
#
# # sum()
# iter_obj = [20, 2, 5, 100]
# print(sum(iter_obj))
# iter_obj = (20, 2, 5, 100)
# print(sum(iter_obj))

#Функция range() для многократно выполняемых действий
#
# print(list(range(7))) # целые числа в диапазоне [0, 7)
# print(list(range(2, 8))) # целые числа в диапазоне [2, 8)
# print(list(range(1, 9, 2))) # целые числа в диапазоне [1, 9) с шагом 2
# print(list(range(1, -7, -2))) # целые числа в диапазоне [1, -7) с шагом -2
# print(list(range(0))) # целые числа в диапазоне (0, 0)
# print(list(range(1, 0))) # целые числа в диапазоне (1, 0)
#
# print('--------')
#
# for el in range(4, 20, 4):
#     res = el / 2
#     print(f"Результат деления {el} на 2: {int(res)}")

#        Область видимости
#локальная
# def full_s_calc():
#     r_val = float(input("Укажите радиус: "))
#     h_val = float(input("Укажите высоту: "))
#     s_side = 2 * 3.14 * r_val * h_val
#     s_circle = 3.14 * r_val ** 2
#     s_full = s_side + 2 * s_circle
#     return s_full
#
# s_val = full_s_calc()
# print(s_val)
# print(s_side)

#глобальная

# def full_s_calc():
#     global r_val, h_val, s_side, s_circle
#     r_val = float(input("Укажите радиус: "))
#     h_val = float(input("Укажите высоту: "))
#     s_side = 2 * 3.14 * r_val * h_val
#     s_circle = 3.14 * r_val ** 2
#     s_full = s_side + 2 * s_circle
#     return s_full
#
# s_val = full_s_calc()
# print(s_val)
# print(s_circle)

#не локальная

# def ext_func():
#     my_var = 0
#     def int_func():
#         my_var += 1
#         return my_var
#     return int_func
#
# func_obj = ext_func()
# print(func_obj)
# print(func_obj())
# print(func_obj())
# print(func_obj())

# def ext_func():
#     my_var = 0
#     def int_func():
#         nonlocal my_var
#         my_var += 1
#         return my_var
#     return int_func
#
# func_obj = ext_func()
# print(func_obj)
# print(func_obj())
# print(func_obj())
# print(func_obj())

