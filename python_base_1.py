# Типы данных (однострочный комментарий)

#Integer (int) - целые числа
a = 5
b = 6
c = a + b
d = a % b
print(c)
print(d)

# Float (float) - вещественные числа
float_a = 0.5
float_b = 1.25
print(type(a))
print(type(float_a))
"""
# Boolean - логический тип данных
is_active = True
is_logout = False

print(is_active or is_logout)
print(is_active and is_logout)
print(not is_active and is_logout)

print(a < b)
print(a > b)
print(a == b)
print(a != b)
print(a <= b)
print(a >= b)

# приведение строки к типу int
age = '15'
year = '2024'
print(int(age) + int(year))

# String (str) - строковый тип данных
text = "love"
text = text + 'a'
text =+ 'a'

# None
flag = None

# Структуры данных
# списки  - list() - []
cars = ['bmv','audi', True, [1,2]]

# словари - dict() - {}
info = {
    'name': 'Alex',
    'cars': cars,
}

# кортежи - tuple - () - неизменяемый список
colors = (
    ('red', '255,0,0'),
    ('blue', '0,0,255')
)

# set - set() - множество - {}
set_numbers = {1,2,3,4,5,5,5,5}

# функции
# файлы
# классы

# Язык регистрозависимый
"""
# многострочный комментарий или длиный текст в переменной
"""
"""
number = 6
print(number)

# ввод  данных из консоли
name = input("Введите свое имя ")
age = input("Введите свой возраст ")