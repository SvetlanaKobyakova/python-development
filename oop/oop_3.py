"""
@classmethod  это метод, который принимает ссылку на сам класс в качестве первого аргумента.
    Он может изменять состояние класса, а не конкретного экземпляра.

@staticmethod - это метод, котрый не принимает ни ссылку на класс, ни ссылку на экземпляр в качестве аргумента.
    Он не может изменять состояние класса или экземпляра. Это функция, которая не принаджеит классу,
    но не зависит от его состояния.

"""

import os

class Person:
    country_of_origin = 'russia'
    count = 0

    @staticmethod
    def check_exist_file(filename):
        if os.path.isfile(filename):
            return True

        raise ValueError ('File not exist')

    @classmethod
    def init_from_birthday(cls, name, birthday):
        age = 2025 - birthday
        return cls(name, age)

    @classmethod
    def edit_country(cls):
        cls.country_of_origin = cls.country_of_origin.title()

    @classmethod
    def incriment_count(cls):
        cls.count += 1

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.incriment_count()

    @classmethod
    def get_object_count(cls):
        return cls.count

    def hello(self):
        print(f'My name is {self.name}')

    def change_age(self, new_age):
        self.age = new_age

    def __add__(self, other):
        return self.age + other.age

    def __str__(self):
        return f'{self.name} {self.age}'
        # return " ".join([self.name, self.age])

person = Person(name='Dima', age=25)
person_2 = Person.init_from_birthday(name='Elena', birthday=1990)

print(person + person_2)