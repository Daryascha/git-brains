# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

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

# функция обработки ответа
def start (answer):
    quantity_dirs = range(1, 10)

    for i in quantity_dirs:
        i = str(i)
        if answer == "1":
            make_dir("dir_" + i)
        elif answer == "2":
            remove_dir("dir_" + i)

def answer ():
    answer = ""
    
    while answer != "3":

        answer = input("Выберите пункт меню:\n"
                       "1. Создать папки\n"
                       "2. Удалить папки\n"
                       "3. Это все ошибка, мне это не нужно\n")
        if answer == "3":
            break
        else: 
            start(answer)

answer()


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def listdir ():
    buffer = os.listdir()
    print("----------------------------------------------")
    print("Список каталогов в директории:")
    for index, element in enumerate(buffer, start=1):
        if os.path.isdir(element):
            print("{}. {}".format(index, element))

listdir()


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import shutil

def current_file_copy ():
    full_name = os.path.basename(__file__)
    name = os.path.splitext(full_name)[0]
    ext = os.path.splitext(full_name)[1]
    copy = name + "_copy" + ext
    if os.path.isfile(copy) != True:
        shutil.copy(full_name, copy)
        print("" + copy + " - создан")
    else:
        print("Файл уже скопирован")

current_file_copy()