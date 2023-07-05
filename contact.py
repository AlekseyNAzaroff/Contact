class Contact:
    def __init__(self, name, phone, email):
        self.__name = name
        self.__phone = phone
        self.__email = email

    def set_name(self, name):
        self.__name = name

    def set_phone(self, phone):
        self.__phone = phone

    def set_email(self, email):
        self.__email = email

    def get_name(self, name):
        return self.__name

    def get_phone(self, phone):
        return self.__phone

    def get_email(self, email):
        return self.__email

    def __str__(self):
        return f'Имя: {self.__name}\nТелефон: {self.__phone}\nЭлектронная почта: {self.__email}'


c1 = Contact('Tom', '6-44-90', 'tom@email.com')
print(c1.__str__())