
import os
import shutil


# функция open(file, mode, encoding) - открывает файл
# file - путь к файлу (абсолютный ли относительно скрипта)
# mode - режим открытия файла
# encoding - кодировка

# основные режимы: r - чтение, w - запись с пересозданием файла, a - добавление в конец файла

myfile = open(file='myfile.txt', mode='w', encoding='utf-8')

# write - запись в файл
myfile.write("Python!!!\n")
text = "Forever!!!\n"
myfile.write(text)
my_list = [' alena,', 'elena!']


# names = "\n".join(my_list)
# myfile.write(names)

for item in my_list:
    myfile.write(item.strip(',! ')+'\n')

# после завершения работы с файлом - закрываем его
myfile.close()

# открытие файла в режиме добавления в конец файла
myfile = open(file='myfile.txt', mode='a', encoding='utf-8')
myfile.write("Python!!!\n")
# myfile.writelines(my_list)   - склеивает список, используется редко
myfile.close()

# открытие файла для чтения
myfile = open(file='myfile.txt', mode='r', encoding='utf-8')
# text_from_file = myfile.read()
# print(text_from_file)
# text_rows = text_from_file.split('\n')
# print(text_rows)

# myfile.seek(0)              # перемещает курсор в начало текста
# text_lines = myfile.readlines()
# # print(text_lines[0], text_lines[1])
# print(text_lines)

# name = 'alex'
# last_name = 'ivanov'
# print(name, last_name, sep='\n')

# mylist = ['alex', 'ivanov']
# print(*mylist, sep='\n')

# Проверка существования пути файла
file_name = 'myfilenew.txt'
if os.path.exists(file_name):
    with open(file=file_name, mode='r', encoding='utf-8') as my_file: #проверяем есть ли такой файл
        text_from_f = my_file.read()                                  # если нет, то
else:
    with open(file=file_name, mode='w', encoding='utf-8') as my_file:
        pass

filename_new = f"new_{file_name}"
if os.path.exists(file_name):
    if not os.path.exists(filename_new):
        os.rename(file_name, filename_new)
        print(f'Файл {file_name} --> {filename_new}')
    else:
        print(f'Файл {filename_new} уже существует')

if os.path.exists(filename_new):
    os.remove(filename_new)
    print(f'Файл {filename_new} удален')

# создание директории
dir_name = 'files'
if not os.path.exists(dir_name):               # с проверкой
    os.makedirs(dir_name, exist_ok=True)

os.makedirs(dir_name, exist_ok=True)        # без проверки

#удаление каталога
# os.rmdir(dir_name)
with open(file=f'{dir_name}/{file_name}', mode='w', encoding='utf-8') as my_file:
    pass

shutil.rmtree(dir_name)

