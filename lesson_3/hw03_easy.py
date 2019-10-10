
__author__ = 'Федорова Д.В.'

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


def my_round(number, ndigits):
    # переводим число в строку
    number_str = str(number)
    # разбиваем число на целую и дробную части
    number_cel, number_drob = number_str.split(".")
    # переводим наши части числа в списки для дальнейшей работы с числами по порядку
    number_cel = [int(d) for d in number_cel]
    number_drob = [int(d) for d in number_drob]

    # обрабатываем список дробной части в обрабтном порядке до нужного количество знаков после запятой
    while len(number_drob) > ndigits:
        if number_drob[-1] >= 5:
            try:
                number_drob[-2] = number_drob[-2] + 1
            # исключение на случай ошибки по индексу
            except IndexError:
                number_cel[-1] = number_cel[-1] + 1
                # в случае если в списке будет стоять 9
                if number_cel[-1] == 10:
                    try:
                        number_cel[-2] = number_cel[-2] + 1
                        number_cel[-1] = 0
                    except IndexError:
                        number_cel.insert(0, 1)
        number_drob = number_drob[:-1]

    while len(number_drob) > 0 and number_drob[-1] == 10:
        try:
            number_drob[-2] = number_drob[-2] + 1
        except IndexError:
            number_cel[-1] = number_cel[-1] + 1
            if number_cel[-1] == 10:
                try:
                    number_cel[-2] = number_cel[-2] + 1
                    number_cel[-1] = 0
                # если это первая цифра после запятой
                except IndexError:
                    number_cel.insert(0, 1)
        # нобходимо чтобы обязательно отработало и мы получили список без последнего элемента для дальнейшей обработки
        finally:
            number_drob = number_drob[:-1]
    # собираем наще число обратно
    number_cel = ''.join([str(x) for x in number_cel])
    number_drob = ''.join([str(x) for x in number_drob])

    return float(number_cel + '.' + number_drob)


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить


def lucky_ticket(ticket_number):
    # переводим число в строку и разбиваем на две части
    ticket_number = str(ticket_number)
    left_part = ticket_number[:3]
    right_part = ticket_number[-3:]

    # функция по подсчету суммы
    def part_sum(str_part):
        counter = 0
        for n in str_part:
            counter += int(n)
        return counter

    if part_sum(left_part) == part_sum(right_part):
        return True
    else:
        return False


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
