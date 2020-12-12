# Задача 1. Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type().
#
different = ['Verona', 2345, 'Parma', False, 23.4]
for element in different:
    print(type(element))

#Задача 2. Для списка реализовать обмен значений соседних элементов (0 и 1, 2 и 3 и т.д).
#
# second = input('Что-нибудь через запятую: ')
# second2 = (second.split(','))
# g = len(second2) // 2 * 2
# second2[0:g:2], second2[1:g:2] = second2[1:g:2], second2[0:g:2]
# print(second2)

#Задача 3. Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Решение через list и через dict.
#
# 3.1. Решение через list
#
# month = int(input('Номер месяца: '))
# four_seasons = ['winter', 'spring', 'summer', 'autumn']
#
# if month in (12, 1, 2):
#     print(four_seasons[0])
# elif month in (3, 4, 5):
#     print(four_seasons[1])
# elif month in (6, 7, 8):
#     print(four_seasons[2])
# elif month in (9, 10, 11):
#     print(four_seasons[3])
# else:
#     print('Набранный Вами месяц не существует, попробуйте снова.')
#
# 3.2. Решение через dict.
#
# month = int(input('Номер месяца: '))
#
# seasons_dict = {1: 'winter', 2: 'spring', 3: 'summer', 4: 'autumn'}
#
# if month in (12, 1, 2):
#     print(seasons_dict.get(1))
# elif month in (3, 4, 5):
#     print(seasons_dict.get(2))
# elif month in (6, 7, 8):
#     print(seasons_dict.get(3))
# elif month in (9, 10, 11):
#     print(seasons_dict.get(4))
# else:
#     print('Набранный Вами месяц не существует, попробуйте снова.')

# Задача 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.
#
# anything = input('Несколько слов разделённых пробелами: ')
# anything2 = (anything.split())
#
# for i in range(len(anything2)):
#     print(i+1, ')', anything2[i][0:10])
#
# Задача 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы
# с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
#
# number = int(input('Введите любое натуральное число: '))
# my_list = [7, 5, 3, 3, 2]
# one_to_one = my_list.count(number)
#
# for element in my_list:
#     if one_to_one > 0:
#         position = my_list.index(number)
#         my_list.insert(position+one_to_one, number)
#         break
#     else:
#         if number > element:
#             position2 = my_list.index(element)
#             my_list.insert(position2, number)
#             break
#         elif number < my_list[len(my_list) - 1]:
#             my_list.append(number)
# print(my_list)

#
# Задача 6.

# prod_n = int(input("Введите количество товаров: "))
# prod_i = 1
# prod_list = list()
# while prod_i <= prod_n:
#     name = input('Название товара №%d: ' % prod_i)
#     price = input('Цена товара: ')
#     quantity = input('Количество: ')
#     ed = input('Единица измерения: ')
#     my_dict = {'название': name, 'цена': price, 'количество': quantity, 'ед': ed}
#     prod_t = (prod_i, my_dict)
#     prod_list.append(prod_t)
#     prod_i += 1
#
# print(prod_list)
#
# analysis_dict = dict()
#
# # print(prod_list[0][1])
# for t in prod_list:
#     tov_dict = t[1]
#     for k in tov_dict.keys():
#         analysis_list = analysis_dict.get(k)
#         if analysis_list is None:
#             analysis_list = list()
#             analysis_dict.update({k: analysis_list})
#         analysis_list.append(tov_dict.get(k))
# print("---")
# print(analysis_dict)




