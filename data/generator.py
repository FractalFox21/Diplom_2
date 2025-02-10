from faker import Faker

class GenerateUsers:
    @staticmethod
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

    @staticmethod
    def generate_fake_email_name():      # метод генерирует словарь с логином, паролем и именем
        fake = Faker()
        email = fake.email()
        name = fake.name()
        fake_user_data = {
            "email": email,
            "name": name}
        return fake_user_data


    @staticmethod
    def generate_fake_email():      # метод генерирует словарь с логином, паролем и именем
            fake = Faker()
            return fake.email()

    @staticmethod
    def generate_fake_name():      # метод генерирует словарь с логином, паролем и именем
            fake = Faker()
            return fake.name()

