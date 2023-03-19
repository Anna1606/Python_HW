import model
import view


def run():
    view.greetings()
    while True:
        view.menu()
        answer = input('Ответ: ')

        if answer == '1':
            view.show_phonebook(model.read_phonebook())

        elif answer == '2':
            model.add_contact(model.find())

        elif answer == '3':
            view.show_phonebook(model.find())

        elif answer == '4':
            model.change_contact(model.find())

        elif answer == '5':
            model.del_contact(model.find())
            model.del_empty_str()

        elif answer == '6':
            break
        