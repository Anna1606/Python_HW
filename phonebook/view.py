import datetime


def greetings():
    now = datetime.datetime.now()
    now = int('%d' % now.hour)
    if now < 6:
        return print('Доброй ночи!')
    elif 6 <= now < 11:
        return print('Доброе утро!')
    elif 11 <= now < 17:
        return print('Добрый день!')
    else:
        return print('Добрый вечер!')


def menu():
    Menu = '''Меню:
    Показать контакты     - нажмите 1
    Добавить контакт      - нажмите 2
    Найти контакт         - нажмите 3
    Редактировать контакт - нажмите 4
    Удалить контакт       - нажмите 5
    Закрыть меню          - нажмите 6
    '''
    return print(Menu)


def show_phonebook(value):
    return print(value)