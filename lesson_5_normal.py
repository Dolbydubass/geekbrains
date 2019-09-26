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
import sys
from lesson_5_easy import show_folders


def folder_manager_choice(choice):
    if choice == 1:
        i = input('Введите название папки: ')
        if i in show_folders():
            os.chdir(i)
            print('Успешно перешел в папку {}'.format(i))
        else:
            print('Невозможно перейти в папку {}'.format(i))
    elif choice == 2:
        empty = [i + '\n' for i in os.listdir()]
        if empty == []:
            print('Папка пустая')
        else:
            print(*empty)
    elif choice == 3:
        print('in progress')
    elif choice == 4:
        # print("current dir = ", os.path.dirname(__file__))
        # print(os.getcwd())
        # print(sys.argv)
        print('in progress')

def folder_manager():
    while True:
        choice = int(input('Выберите пункт:\n'
                           '1. Перейти в папку\n'
                           '2. Просмотреть содержимое текущей папки\n'
                           '3. Удалить папку\n'
                           '4. Создать папку\n'
                           '5. Выход\n'
                           '---------------------\n'
                           'Ваш выбор:'))
        if choice == 5:
            break
        folder_manager_choice(choice)

folder_manager()


