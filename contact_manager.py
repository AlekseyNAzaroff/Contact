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
    pass

def get_menu_choice():
    pass