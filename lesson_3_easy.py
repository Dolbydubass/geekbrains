# Постарайтесь использовать то, что мы прошли на уроке при решении этого ДЗ,
# вспомните про zip(), map(), lambda, посмотрите где лучше с ними, а где они излишни!

# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"

print('Задача 1.')

def info(name, age, city):
    return '{}, {} год(а), проживает в городе {}'.format(name, age, city)


print(info('Валера', 27, 'Пермь'))


# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них

print('Задача 2.')

def big_one(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
    # return max(a, b, c)  # Более простой способ, но поучается что функция делает другую функцию)


print(big_one(3, 7, 1))  # Для проверки


# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов

print('Задача 3.')

def long_one(*args):
    return max(*args, key=len)


print(long_one('zz', 'aaaa', '123','hello_world'))