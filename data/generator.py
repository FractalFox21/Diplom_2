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
    def generate_fake_email():      # метод генерирует email
            fake = Faker()
            return fake.email()

    @staticmethod
    def generate_fake_name():      # метод генерирует имя
            fake = Faker()
            return fake.name()

    # метод возвращает словарь со сгенерированными данными для пароля и имени
    @staticmethod
    def generating_user_data_no_email():
        fake = Faker()
        password = fake.password()
        name = fake.name()
        reg_data = {"password": password, "name": name}
        return reg_data

    @staticmethod
    def generating_user_data_no_pass():
        fake = Faker()
        email = fake.email()
        name = fake.name()
        reg_data = {"email": email, "name": name}
        return reg_data

    @staticmethod
    def generating_user_data_no_name():
        fake = Faker()
        email = fake.email()
        password = fake.password()
        reg_data = {"email": email, "password": password}
        return reg_data
