# Задача 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.

def get_quotient(dividend, divider):
    if divider == 0:
        return print('Ошибка: делитель равен нулю')
    else:
        quotient = dividend / divider
        return quotient

print(get_quotient(10, 5))

# Задача 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def get_user_data(name, surname, d_of_brd, city, email, phone):
    return str(f'{name}, {surname}, {d_of_brd}, {city}, {email}, {phone}')

print (
get_user_data(
    name = 'Алексей',
    surname = 'Синельцев',
    d_of_brd = '23.11.1987',
    city = 'Саратов',
    email = 'aleksej-sinelcev@yandex.ru',
    phone = '89271100957'
)
)

#Задача 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def get_summ_max(arg1, arg2, arg3):
    arg_list = [arg1, arg2, arg3]
    max1 = max(arg_list)
    arg_list.remove(max1)
    max2 = max(arg_list)
    return max1 + max2


print(get_summ_max(7,8,3))

# Задача 4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y). При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

def get_exp(num, exp):
    x, num, exp = 1, float(num), int(exp)
    if num <= 0:
        err1 = 'Необходимо ввести положительное число аргумента num'
        return err1
    elif exp >= 0:
        err2 = 'Необходимо ввести целое отрицательное число аргумента exp'
        return err2
    else:
        #Решаю более сложный способ с помощью итерационной формулы Герона
        while round(x ** abs(exp), 2) != num:
            x = 1 / abs(exp) * ((abs(exp) - 1) * x + num / x ** (abs(exp) - 1))
        return round(x, 4)

print(get_exp(123, -3))

# Задача 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел
# к полученной ранее сумме и после этого завершить программу.

def get_sum(*args):
    num_list = []
    while True:
        args = input('Введите числа, разделенные пробелами: ')
        num_list.extend(args.split(' '))
        if args.find('/') != -1:
            break
    print(
        sum(map(lambda x: int(x), num_list[:num_list.index('/')]))
    )

get_sum()

# Задача 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text. Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().

def int_func(word):
    alf, out_flg = 'abcdefghijklmnopqrstuvwxyz', True
    for w in word:
        if w not in alf:
            print('Должно быть написано одно слово маленькими латинскими буквами')
            out_flg = False
            break
    if out_flg == True:
        return word.title()


def int_func_ap(int_func, word_str):
    alf, out_flg = 'abcdefghijklmnopqrstuvwxyz ', True
    for w in word_str:
        if w not in alf or word_str.find(' ') == -1:
            print('Должны быть введены слова через пробелы маленькими латинскими буквами')
            out_flg = False
            break
    if out_flg == True:
        word_list = word_str.split(' ')
        return ' '.join(list(map(int_func, word_list)))


print(int_func_ap(int_func, 'in vino veritas in aqua sanitas'))