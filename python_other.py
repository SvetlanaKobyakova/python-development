# # int_numbers = []
# # for i in range(10):
# #     int_numbers.append(i)
# # print(int_numbers)
#
# int_numbers = [n for n in range(10)]                    # генератор чисел от 0 до 10
# # print(int_numbers)
#
# int_numbers = [n for n in range(10) if n % 2 == 0]      #генератор четных чисел
# # print(int_numbers)
#
# numbers = [ -3, -2, 1, 3, 5]
# pos_numbers = []
# for i in numbers:
#     if i > 0:
#         pos_numbers.append(i)
# # print(pos_numbers)
#
# # list comprehension
# pos_numbers_2 = [n for n in numbers if n > 0]       # добавить числа больше 0
# pos_numbers_2 = [n for n in numbers if n % 2 == 0]  # добавить четные числа
# # print(pos_numbers_2)
#
# def print_hello(lang: str):
#     if lang == 'ru':
#         print('Привет')
#     elif lang == 'en':
#         print("Hello")
#     elif lang == 'ge':
#         print('Hallo')
#     else:
#         print('err')
#
# def print_hello_match(lang: str):
#     match lang:
#         case 'ru': print('Привет')
#         case 'en': print('Hello')
#         case 'ge': print('Hallo')
#         case _:    print('err')
#
# print_hello(lang='ru')
# print_hello(lang='en')
# print_hello(lang='bb')

def print_main_menu():
    while True:
        print('Выберите необходимое действие')
        print('1. Посмотреть список книг')
        print('2. Добавить книгу')
        print('3. Найти книгу')
        print('4. Удалить книгу')
        action = input('>>> ')

        match action:
            case '1':
                book_list()
                break
            case '2': book_add()
            case '3': book_search()
            case '4': book_delete()
            case 'exit':
                print ('До свидания')
                exit()
            case _: print('Введите цифру от 1 до 4 или exit ля выхода')

def book_list():
    print('Список книг:')

def book_add():
    print('Введите название и автора книги:')
    action = input('>>> ')

def book_search():
    print('Введите название и автора книги:')
    action = input('>>> ')

def book_delete():
    print('введите ID книги для удаления:')
    action = input('>>> ')

print_main_menu()