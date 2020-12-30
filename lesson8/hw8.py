# # 1

class Date:
    def __init__(self, date_str):
        self.date_str = date_str

    def __str__(self):
        return self.date_str

    @classmethod
    def get_numbers(cls, date):
        str_numbers = date.date_str.split("-")
        return [int(str_numbers[0]), int(str_numbers[1]), int(str_numbers[2])]

    @staticmethod
    def check_date(date):
        try:
            str_numbers = date.date_str.split("-")
            day = int(str_numbers[0])
            month = int(str_numbers[1])
            year = int(str_numbers[2])
            if day < 1:
                return False
            elif day > 31:
                return False
            if month < 1:
                return False
            elif month > 12:
                return False
        except Exception:
            return False
        return True


date = Date("29-12-2020")
print(Date.get_numbers(date))
check_result = Date.check_date(date)
if check_result:
    print(f"Дата '{date}' верная")
else:
    print(f"Дата '{date}' некорректна")


# # 2.
class NewException(Exception):
    def __init__(self, text):
        self.text = text


def division(a, b):
    if b == 0:
        raise NewException("Делить на 0 нельзя!!!")
    return a / b


a_1 = int(input("Введите делимое: "))
b_1 = int(input("Введите делитель: "))

try:
    print(division(a_1, b_1))
except Exception as err:
    print(type(err), err)


# # 3

class NotNumberException(Exception):
    def __init__(self, text1):
        self.text = text1

    @classmethod
    def check_list(cls, num_list):
        for x in num_list:
            try:
                int(x)
            except Exception:
                raise cls(f"Обнаружено не число:{x}")


input_list = []

while True:
    el = input("Введите элемент списка:")
    if el == "stop":
        break
    else:
        input_list.append(el)

try:
    NotNumberException.check_list(input_list)
except Exception as err:
    print(type(err), err)


# 4, 5, 6
class Warehouse:
    def __init__(self, main_dict):
        self.main_dict = main_dict

    def __str__(self):
        return str(self.main_dict)

    def add_office_equipment(self, department, office_equipment):
        dep_list = self.main_dict.get(department)
        if dep_list is None:
            dep_list = []
            self.main_dict[department] = dep_list
        office_equipment.check_data()
        dep_list.append(office_equipment)

    def report(self):
        count_dict = dict()
        for dep in self.main_dict.keys():
            print(f"Техника подразделения '{dep}':")
            office_equipment = self.main_dict[dep]
            count_dict_dep = dict()
            for e in office_equipment:
                class_name = e.__class__.__name__
                count_e = count_dict_dep.get(class_name)
                if count_e is None:
                    count_dict_dep[class_name] = 1
                else:
                    count_dict_dep[class_name] += 1

                count_dep = count_dict.get(class_name)
                if count_dep is None:
                    count_dict[class_name] = 1
                else:
                    count_dict[class_name] += 1
            print(count_dict_dep)
        print("Общая статистика:")
        print(count_dict)


class Office_equipment:
    def __init__(self, weight, page_speed):
        self.weight = int(weight)
        self.page_speed = int(page_speed)

    def check_data(self):
        if self.weight < 0:
            raise Exception("Неверный вес")
        if self.page_speed < 0:
            raise Exception("Неверная скорость")


class Printer(Office_equipment):
    def __init__(self, weight, page_speed, print_type):
        super().__init__(weight, page_speed)
        self.print_type = print_type

    def check_data(self):
        super().check_data()
        if self.print_type not in ["Струйный", "Лазерный"]:
            raise Exception("Неверный тип принтера")


class Scanner(Office_equipment):
    def __init__(self, weight, page_speed, scan_type):
        super().__init__(weight, page_speed)
        self.scan_type = scan_type

    def check_data(self):
        super().check_data()
        if self.scan_type not in ["Цветной", "Монохромный"]:
            raise Exception("Неверный тип сканера")


class Xerox(Office_equipment):
    def __init__(self, weight, page_speed, xerox_type):
        super().__init__(weight, page_speed)
        self.xerox_type = xerox_type

    def check_data(self):
        super().check_data()
        if self.xerox_type not in ["Матричный"]:
            raise Exception("Неверный тип ксерокса")


warehouse = Warehouse(dict())

printer_1 = Printer(1, 5, "Струйный")
printer_2 = Printer(3, 20, "Лазерный")

scanner_1 = Scanner(1, 3, "Цветной")

xerox_1 = Xerox(1, 10, "Матричный")

warehouse.add_office_equipment("Отдел кадров", printer_2)
warehouse.add_office_equipment("Отдел кадров", xerox_1)
warehouse.add_office_equipment("Канцелярия", printer_1)
warehouse.add_office_equipment("Канцелярия", scanner_1)

warehouse.report()


# 7
class MyСomplex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return str(f"{self.x} {self.y}*i")

    def __add__(self, other):
        return MyСomplex(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return MyСomplex(self.x * other.x - self.y * other.y, self.x * other.y + self.y * other.x)


mycomplex_1 = MyСomplex(1, 5)
mycomplex_2 = MyСomplex(1, -1)
mycomplex_3 = MyСomplex(2, 3)

print(mycomplex_1 + mycomplex_2 + mycomplex_3)
print(mycomplex_1 * mycomplex_2 * mycomplex_3)
