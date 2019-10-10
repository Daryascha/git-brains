
__author__ = 'Федорова Д.В.'

# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.

import re

line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO'\
       'GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK'\
       'TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn'\
       'LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXa'\
       'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete'\
       'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ'\
       'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb'\
       'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC'\
       'EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB'\
       'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuT'\
       'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu'\
       'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB'\
       'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa'\
       'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ'\
       'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'
# с помощью re
line_low = re.findall(r"[a-z]+", line)
print("Символы в нижнем регистре с использованием модуля re: \n",line_low)
print("------------------------------------------------------------------------")


# без re
# Преобразуем список из кодов ANSI в список букв A-Z
symbol = list(map(lambda x: chr(x), list(range(65,91))))
line_new = list(line)
 
for i, element in enumerate(line_new[:]):
    for element_2 in symbol:
        if element == element_2:
            line_new[i] = " "
 
# Соединение списка в строку методом .join и разбиение строки по символу ' '
s_string="".join(line_new).split(" ")
 
line_low2 = [i for i in s_string if i != ""]
print("Символы в нижнем регистре без использованием модуля re: \n",line_low2)
print("------------------------------------------------------------------------")


# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа - два символа в верхнем регистре.
# Т.е. из строки 
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.

line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysm'\
       'NOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewV'\
       'fzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSA'\
       'HqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIV'\
       'jXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnW'\
       'etekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfC'\
       'vzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbR'\
       'uXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkm'\
       'jCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOn'\
       'LfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGS'\
       'euTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCf'\
       'KCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWH'\
       'uXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQN'\
       'JFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQ'\
       'oiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'

# с помощью re
line_2_str = re.findall(r"[a-z]{2}([A-Z]+)[A-Z]{2}", line_2)
print("Список с использованием модуля re: \n",line_2_str)
print("------------------------------------------------------------------------")
 
# без re
# Преобразуем список из кодов ANSI в список букв A-Z
symbol_1 = list(map(lambda x: chr(x), list(range(65, 91))))
# Преобразуем список из кодов ANSI в список букв a-z
symbol_2 = list(map(lambda x: chr(x), list(range(97, 123))))  
line_new = list(line_2)

list_1 = []
i = len(line_new) - 1
# Находим  символ в верхнем регистре после которого стоят еще два символа в верхнем регистре
while i >= 0:
       if line_new[i] in symbol_2:
              list_1.append(line_new[i])
       elif line_new[i] in symbol_1 and i <= len(line_new) - 3 and line_new[i + 1] in symbol_1 and line_new[
              i + 2] in symbol_1:
              list_1.append(line_new[i])
       else:
              list_1.append(' ')
       i -= 1
list_1.reverse()  # Переворачиваем список

i = 0
list_2 = []
# Начальное условие поиска сортировки символов в верхнем регистре
registr = True  
# Фильтрация списка.
while i <= len(list_1) - 1:
       if list_1[i] in symbol_2:
              registr = True
       if list_1[i] in symbol_1 and list_1[i - 1] in symbol_2 and list_1[i - 2] in symbol_2:
              list_2.append(list_1[i])
              registr = False
       elif list_1[i] in symbol_1 and registr == False:
              list_2.append(list_1[i])
       else:
              list_2.append(" ")
       i += 1
stroka = "".join(list_2).split(" ")  # Преобразование в строку и разбиение по пробелам

line_str_3 = [i for i in stroka if i != ""]  # Формирование выхрдного списка из строки
print("Список без использованием модуля re: \n", line_str_3)
print("------------------------------------------------------------------------")

# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.

import random
import itertools

a = [random.randint(0,9) for _ in range(2500)]
str_1 = ''.join(str(i) for i in a) 

with open("test.txt", 'w', )  as file_1: 
    file_1.write(str_1) 

print(max((list(g) for k, g in itertools.groupby(a)), key=len))