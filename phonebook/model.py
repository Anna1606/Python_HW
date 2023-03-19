
def read_phonebook():
    with open('phonebook\phonebook.txt', 'r', encoding='utf-8') as file:
        text = file.read()

    return text


def read_lines():
    with open('phonebook\phonebook.txt', 'r', encoding='utf-8') as file:
        text = file.readlines()

    return text


def add_contact():
    surname = input('Введите Фамилию: ')
    name = input("Имя: ")
    fathername = input('Отчество: ')
    number = input('номер телефона: ')
    with open('phonebook\phonebook.txt', 'a', encoding='utf-8') as file:
        file.write(f'\n{surname} {name} {fathername} {number}')

    return print('Контакт успешно добавлен')


def find_all():
    find = input('Введите фамилию: ')
    text = read_lines()
    find_ = {}
    for i, v in enumerate(text):
        if find in v:
            find_[i] = v

    return find_


def find():
    find = find_all()
    if find != None:
        for i, str in find.items():
            print(f'{i} - {str}')
        s = int(input("Укажите нужный номер п/п контакта: "))
        text = read_lines()

        return text[s]
    else:
        return 'Такого контакта не существует'


def change_contact(find_one):
    lines = read_lines()
    for i, line in enumerate(lines):
        if find_one == line:
            old = input('Что меняем: укажи начальное значение: ')
            lines[i] = line.replace(old, input('Укажи новое значение: '))
    with open('phonebook\phonebook.txt', 'r+', encoding='utf-8') as file:
        file.writelines(lines)


def del_contact(find_one):
    lines = read_lines()
    with open('phonebook\phonebook.txt', 'w', encoding='utf-8') as file:
        for line in lines:
            if find_one not in line:
                file.write(line)

def del_empty_str():
    lines = read_lines()
    lines = [line for line in lines if line.strip()] # создаем новый список, в котором только непустые строки
                                                     # метод strip() удаляет все пробельные символы из начала и конца строки 
    with open('phonebook\phonebook.txt', 'w', encoding='utf-8') as file:
        file.writelines(lines)
