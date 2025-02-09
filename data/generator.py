from faker import Faker


def generate_fake_user():      # метод генерирует словарь с логином, паролем и именем
        fake = Faker()
        email = fake.email()
        password = fake.password()
        name = fake.name()
        fake_user_data = {
            "email": email,
            "password": password,
            "name": name}
        return fake_user_data



