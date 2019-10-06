
__author__ = 'Федорова Д.В.'

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1


def fibonacci(n, m):
    a, b = 1, 1
    f_list = [1, ]

    for i in range(m):
        a, b = b, a + b
        f_list.append(a)

    return f_list[n - 1:m]

x = int(input("введите целое число - с какого элемента начнем ряд: "))
y = int(input("введите целое число - каким элементом закончим ряд: "))

print("числа фибоначчи от " + str(x) + " до " + str(y) + ": ", fibonacci(x, y))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


from random import randint

def bubble(array):
    for i in range(N - 1):
        for j in range(N - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

#создаем наш список
N = int(input("введите количество чисел генерируемое для списка: "))
a = []
for i in range(N):
    a.append(randint(1, 99))

print("до сортировки: ",a)
bubble(a)
print("после сортировки: ",a)

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


from random import randint

# создаем наш список
N = int(input("введите количество чисел генерируемое для списка: "))
seq = []
s = ""
for i in range(N):
    seq.append(randint(1, 99))

# функция фильтрации, в нее передаем функцию фильтрации и наш список чисел
def filter_func(fun, iterable):
    res = []
    for i in iterable:
        if fun(i):
            res.append(i)
    return res

# функция фильтр
def fun(x):
    if x % 2 == 0:
        return True
    else:
        return False

print("наш сгенерированный список: ", seq)
result = filter_func(fun, seq)
print("результат: ", result)


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.


from math import sqrt

def is_parallelogram(x1, y1, x2, y2, x3, y3, x4, y4):
    if dlina_storony(x1, y1, x2, y2) == dlina_storony(x4, y4, x3, y3) and dlina_storony(x2, y2, x3, y3) == dlina_storony(x1, y1, x4, y4) and proverka_tochek(x1, y1, x2, y2, x3, y3, x4, y4) == False:
        return True
    else:
        return False

# считаем длину стороны
def dlina_storony(xa, ya, xb, yb):
    return sqrt((xb - xa) * (xb - xa) + (yb - ya) * (yb - ya))

# отклонение C от AB
def otklonenie(x1, y1, x2, y2, x3, y3):
    AB = dlina_storony(x1, y1, x2, y2)
    A = (y2 - y1) / AB
    B = (x2 - x1) / AB
    C = (x1 * (y2 - y1) - y1 * (x2 - x1)) / AB
    return (x3 * A - y3 * B - C)

# проверка нахождения точек на одной прямой
def proverka_tochek(x1, y1, x2, y2, x3, y3, x4, y4):
    devAB_C = otklonenie(x1, y1, x2, y2, x3, y3)
    devAB_D = otklonenie(x1, y1, x2, y2, x4, y4)
    devBC_D = otklonenie(x2, y2, x3, y3, x4, y4)
    devAC_D = otklonenie(x1, y1, x3, y3, x4, y4)

    if devAB_C == 0 or devAB_D == 0 or devBC_D == 0 or devAC_D == 0:
        return True
    else:
        return False

# заполняем координаты
x1, y1, x2, y2, x3, y3, x4, y4 = (int(input("введите поочередно координаты x1, y1, x2, y2, x3, y3, x4, y4: ")) for _ in range(8))

res = is_parallelogram(x1, y1, x2, y2, x3, y3, x4, y4)

if res == True:
    print("Это параллелограм!)")
else:
    print("Это вам не параллелограм :Р")
