# #  словарь определяется функцией dict  или  литералом {}
# #  словарь хранит данные в формате ключ: значение
# from os import remove
#
# mydict = dict()
# name = 'NAME'
# person = {}
# person_2 = {'name': 'Elena', 'age': 26}
#
# # получение элемента из словаря ИМЯ_СЛОВАРЯ[КЛЮЧ]
# print(person_2['name'])
#
# # добавление элемента в словарь ИМЯ_СЛОВАРЯ[КЛЮЧ]=ЗНАЧЕНИЕ
# person_2['phone'] = '123456789'
# print(person_2)
#
# person_2['age'] = 45
# print(person_2)
#
# print(len(person_2))
# person_2['language'] = {'main': 'Russian', 'other': 'English'}
# person_2['age'] = ['11111111', '22222222', '333333']
#
# print(person_2)
#
# person_2[100] = ['11111111', '22222222', '333333']
# print(person_2)
#
# print(person_2.keys())
# print(list(person_2.keys())[0])
# print(list(person_2.values()))
#
# for key in person_2.keys():
#     print(key)
#
# for key in person_2.values():
#     print(key)
#
# for key in person_2:
#     print(key, person_2[key])
#
# for item in person_2.items():
#     print(item)
#
# for key, value in person_2.items():
#     print(f"key - {key}, value - {value}")
#
# for key in person_2:
#     print(f"key - {key}, value - {person_2[key]}")
#
# print(len(person_2))
#
# print(person_2.get('jjjjj', {}).get('kkkkk', {}))
# age = person_2.pop('age')
# print(age)
# print((person_2))
#
# del person_2[100]
# print(person_2)
#
# person_1 = person_2
# print(id(person_1))
# print(id(person_2))
#
# person_2['NEW'] = 'NEW'
# print(person_1)
# print(person_2)
#
# print(person_2.popitem())
# print(person_2.popitem())
#
# month_dict = {}
# month = [1,2,3,4,5,6,7,8,9,10,11,12]
# for i in month:
#     month_dict[i] = f'Month - {i}'
# print(month_dict)


users_info = []
N = 3

for i in range(N):
    print(f"Enter {i+1} user`s info")
    name = input("Введите имя")
    age = input("Введите возраст")
    phone = input("Номер телефона")
    info = {"name": name,
            "age": age,
            "phone": phone
            }
    users_info.append((info))

print(users_info)



# x = 5
# y = 6
# x,y = y,x

# print(x)
# print(y)

# name, age = ('Sasha', 25)

# print(name)
# print(age)

