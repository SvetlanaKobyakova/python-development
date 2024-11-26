# def get_info(name,age):
#     print(name.title())
#     print(age)
#
# get_info(name = 'alex', age = 27)
#
#
# a = [1,2,3]
# b = [*a, 4,5,6]                 # *-оператор распаковки
# print(b)
#
# def print_scores(name, *scores):            # *scores(неизвестный параметр) - упаковывает
#     print(f"name - {name}")
#     for i in scores:
#         print(i)
#
# print_scores('Dima',26, 25, 65)

# def func(*args, **kwargs):            # *args- позиционные аргументы, **kwargs- именованные аргуметы
#     print(args)
#     pass                    # заглушка

def print_pet_names(owner, **pets):
    print(f'Владелец - {owner}')
    # for key, value in pets.items():
    #     print(f"{key} - {value}")
# или
    for key in pets:
        print(f"{key} - {pets[key]}")

print_pet_names(owner="Dima", dog="Tima", cat="Barsik")
