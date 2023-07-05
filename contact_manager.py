import contact
import pickle

LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

FILENAME = 'cntacts_dat'


def main():
    mycontacts = load_contacts()
    choice = 0

    while choice != QUIT:
        choice = get_menu_choice

        if choice == LOOK_UP:
            look_up(mycontacts)
        elif choice == ADD:
            add(mycontacts)
        elif choice == CHANGE:
            change(mycontacts)
        elif choice == DELETE:
            delete(mycontacts)

    save_contacts(mycontacts)


def load_contacts():
    try:
        input_file = open(FILENAME, 'rb')
        contact_dct = pickle.load(input_file)
        input_file.close()
    except IOError:
        contact_dct = {}

    return contact_dct


def get_menu_choice():
    print()
    print('Меню')
    print('----------------------')
    print('1. Найти контакт')
    print('2. Добавить контакт')
    print('3. Изменить контакт')
    print('4. Удалить контакт')
    print('5. Выйти из программы')
    print()

    choice = int(input('Введите выбранный пункт: '))
    while choice < LOOK_UP > QUIT:
        choice = int(input('Введите выбранный пункт: '))

    return choice


def look_up(mycontacts):
    name = input('Введите имя: ')
    print(mycontacts.get(name, 'Это имя не найдено.'))


def add(mycontacts):
    name = input('Имя: ')
    phone = input('Телефон: ')
    email = input('Электронный адрес: ')

    entry = contact.Contact(name, phone, email)

    if name not in contact:
        mycontacts[name] = entry
        print('Контакт добавлен.')
    else:
        print('Такой контакт уже существует.')


def change(mycontacts):
    name = input('Введите имя: ')

    if name in mycontacts:
        phone = input('Введите новый номер телефона: ')
        email = input('Введите новый адрес электронной почты: ')
        entry = contact.Contact(name, phone, email)
        mycontacts[name] = entry
        print('Контакт обновлен.')
    else:
        print('Это имя не найдено.')


def delete(mycontacts):
    name = input('Введите имя: ')
    if name in contact:
        del mycontacts[name]
        print('Контакт удален.')
    else:
        print('Такой контакт не найден.')


def save_contacts(mycontacts):
    output_file = open(FILENAME, 'wb')
    pickle.dump(mycontacts, output_file)
    output_file.close()


if __name__ == '__main__':
    main()
