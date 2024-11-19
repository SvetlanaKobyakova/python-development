# создание списка
# с использованием функции list()
users = list()
# с использованием литерала []
#             0    1(-2)   2(-1)
users_2 = ['Dima','Vova','Elena']

#  доступ к элементам списка
print(users_2[0])
print(users_2[-1])
print(users_2[1])


#  добавление элемента в список
users_2.append('Olga')
print(users_2)

# расширение списка элементами другого списка
users_2 +=['Sasha','Masha']
users_2.extend(['Natasha','Sveta', 'Sasha'])
print(users_2)

# добавление элемента в произвольное место
users_2.insert(0, 'Zerro')
users_2.insert(-1, 'Last')
users_2.insert(len(users_2), 'Last!!!')
print(users_2)

# получение количества элементов списка
print(len(users_2))

# рор - удалить элемент и получить его
#element = users_2.pop(0)
#print(element)
print(users_2.pop())
print(users_2)

# count - подсчет количества элементов в списке
print(users_2.count('Sasha'))

#users_2.remove('Sasha') (первого, которого нашел)
print(users_2)

# получение индекса элемента по его значению (первого, которого нашел)
print(users_2.index('Sasha', 4, 7))

# очищение списка
#users_2.clear()
#print(users_2)

users_3 = [1, 2, 3, 3]
print(users_2 + users_3)

# оператор для проверки вхождения элемента в список
name = 'Sasha'
if name in users_2:
    print('ok')
else:
    print('not found')

name = 'sasha'
if name not in users_2:
    print('ok')
else:
    print('not found')