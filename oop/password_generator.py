import random
import string


class PasswordGenerator:
    special_chars = '!#&$%()_*@'

    def __init__(self,
                 min_lenght=6,
                 max_lenght=12,
                 use_uppercase=True,
                 use_special_chars=True):
        self.min_lenght = min_lenght
        self.max_lenght = max_lenght
        self.use_uppercase = use_uppercase
        self.use_special_chars = use_special_chars

    def generate_password(self):
        if self.min_lenght > self.max_lenght:
            raise ValueError('Минимальная длина не может быть больше максимальной')

        length = random.randint(self.min_lenght, self.max_lenght)

        characters = string.ascii_lowercase + string.digits

        if self.use_uppercase:
            characters += string.ascii_uppercase

        if self.use_special_chars:
            characters += PasswordGenerator.special_chars

        password = "".join(random.choice(characters) for _ in range(length))
        return password

password_generator = PasswordGenerator()
print(password_generator.generate_password())


