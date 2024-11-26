# def sum_numbers(a, b):
#     return a + b
#
# result = sum_numbers(5, 4)
# print(result)
#
# double = lambda x: x**2
# print(double(2))
#         # или
# def double(x):
#     if x.isdigit():
#         return int(x)**2
#     else:
#         return 0
from functools import reduce

# list_of_numbers = ['1', '234', '234', '22', '11', 'ggg']
#
# list_int_numbers = list(map(int, list_of_numbers))
# list_double_numbers = list(map(double, list_int_numbers))
# list_double_numbers = list(map(lambda x: int(x)**2, list_int_numbers))
#
# print(list_double_numbers)
# print(list_int_numbers)
# или
# list_int_numbers = []

# for i in list_of_numbers:
#     if i.isdigit():
#         list_int_numbers.append(int(i))
# print(list_of_numbers)
# print(list_int_numbers)

# users = [['alex', 70], ['dima', 50], ['elena', 30],['sveta', 25]]
# old_users = list(filter(lambda user: user[-1] > 30, users))
# print(old_users)

# old_users = []
# for i in users:
#     if i[1] > 30:
#         old_users.append(i)
#
# print(old_users)

list_of_numbers = ['1', '234', '234', '22', '11']
sum_numbers = reduce(lambda x,y: int(x) + int(y), list_of_numbers)
print(sum_numbers)