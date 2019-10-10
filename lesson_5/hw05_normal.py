# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py


import os

# меняем путь
def change_dir (path):
    try:
        os.chdir(path)
    except FileNotFoundError:
        print("{} - каталога не существует".format(path))

def up_dir ():
    os.chdir(os.path.abspath(os.path.join(__file__ ,"..")))     

# функция добавления дириктории
def make_dir (name):
    try:
        os.makedirs(name)
    except FileExistsError:
        print("{} - уже существует".format(name))

# функция удаления указанной дириктории
def remove_dir (name):
    try:
        os.removedirs(name)
    except FileNotFoundError:
        print("{} - папки не существует".format(name))

def listdir ():
    buffer = os.listdir()
    print("----------------------------------------------")
    print("Список каталогов в директории:")
    for index, element in enumerate(buffer, start=1):
        if os.path.isdir(element):
            print("{}. {}".format(index, element))                

def start (answer):

    if answer == "1":
        path_name = input("Укажите папку для перехода: ")
        change_dir(path_name)
    elif answer == "2":
        up_dir()    
    elif answer == "3":
        listdir()
    elif answer == "4":
        name = input("Введите имя удаляемой папки: ")
        remove_dir(name)
    elif answer == "5":
        name = input("Введите имя новой папки: ")
        make_dir(name) 

def answer():
    answer = ""
    
    while answer != "6":

        print('Текущая директория: ' + os.getcwd())
        answer = input("Выберите пункт меню:\n"
                       "1. Перейти в папку\n"
                       "2. Перейти на уровень вверх\n"
                       "3. Помотреть содержимое текущей папки\n"
                       "4. Удалить папку\n"
                       "5. Создать папку\n"
                       "6. Выход\n")
        if answer == "6":
            break
        else: 
            start(answer)

answer()