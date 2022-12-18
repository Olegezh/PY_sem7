from import_data import import_data
from export_data import export_data
from print_data import print_data

def input_data():
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    phone_number = input("Введите номер телефона: ")
    note = input("Введите описание: ")
    return [last_name, first_name, phone_number, note]

def choice_sep():
    sep = input("Введите разделитель: ")
    if sep == "":
        sep = None
    return sep

def choice_todo():
    print("Выберите операцию с телефонной книгой:\n\
    1 - импорт;\n\
    2 - экспорт;")
    ch = input("Введите цифру: ")
    if ch == '1':
        sep = choice_sep()
        import_data(input_data(), sep)
    else:
        data = export_data()
        print_data(data)
