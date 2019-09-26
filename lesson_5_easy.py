# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
import sys

def new_folders():
    return [os.mkdir('dir_' + str(i)) for i in range(1, 10)]


def del_new_folders():
    return [os.removedirs('dir_' + str(i)) for i in range(1, 10)]


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def show_folders():
    return [i for i in os.listdir() if os.path.isdir(i)]


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copy_file():
    file = os.path.basename(*sys.argv)
    return os.system('cp {} copy_{}'.format(file, file))
