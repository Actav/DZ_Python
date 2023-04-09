# №8.1[49]. Создать телефонный справочник с возможностью импорта и экспорта
# данных в формате .csv
# Информация о человеке:
# Фамилия, Имя, Телефон, Описание
# Корректность и уникальность данных не обязательны.
# Функционал программы
# 1) телефонный справочник хранится в памяти в процессе выполнения кода.
# Выберите наиболее удобную структуру данных для хранения справочника.
#
# 2) CRUD: Create, Read, Update, Delete
# Create: Создание новой записи в справочнике: ввод всех полей новой записи,
# занесение ее в справочник.
#
# Read: он же Select. Выбор записей, удовлетворяющих заданном фильтру:
#   по первой части фамилии человека. Берем первое совпадение по фамилии.
#
# Update: Изменение полей выбранной записи. Выбор записи как и в Read,
#   заполнение новыми значениями.
#
# Delete: Удаление записи из справочника. Выбор - как в Read.
#
# 3) экспорт данных в текстовый файл формата csv
#
# 4) импорт данных из текстового файла формата csv
#
# Используйте функции для реализации значимых действий в программе
# Усложнение.
# - Сделать тесты для функций
# - Разделить на model-view-controller


from os import path

phonebook = {}
phonebook_last_id = 0


def create(
        db: dict,
        _id: int,
        surname: str,
        name: str,
        phone: str,
        description: str) -> tuple:  # data_base
    db[_id] = {
        "surname": surname,
        'name': name,
        'phone': phone,
        'description': description,
    }

    return db, _id + 1


def read(db: dict, surname_filter: str) -> int:
    surname_filter = surname_filter.lower()
    for _id in db:
        if db[_id]['surname'].lower().find(surname_filter) == 0:

            return _id


def update(db: dict, found_id: int) -> None:
    print_record(db, found_id)

    if found_id is not None:
        if get_confirm("Обновить запись запись?"):
            surname, name, phone, description = get_user_data()
            db[found_id] = {
                "surname": surname,
                'name': name,
                'phone': phone,
                'description': description,
            }
            print_message("ЗАПИСЬ ОБНОВЛЕНА")


def delete(db: dict, found_id: int) -> None:
    print_record(db, found_id)

    if found_id is not None:
        if get_confirm("Удалить запись?"):
            del db[found_id]
            print_message("ЗАПИСЬ УДАЛЕНА")


def export_db(db: dict, file_name: str, delimiter: str = '#') -> None:
    file_name = f"{file_name}.csv"
    with open(file_name, "w", encoding='utf-8') as file:
        for _, data in db.items():
            data_line = delimiter.join(data.values())
            file.write(f"{data_line}\n")


def import_db(
        db: dict,
        last_id: int,
        file_name: str,
        delimiter: str = '#') -> tuple:
    file_name = f"{file_name}.csv"
    if path.exists(file_name) and path.isfile(file_name):
        with open(file_name, "r", encoding='utf-8') as file:
            for line in file:
                # data['surname']},{data['name']},{data['phone']},{data['description']}
                _data = line.strip().split(delimiter)
                db[last_id] = {
                    'surname': _data[0],
                    'name': _data[1],
                    'phone': _data[2],
                    'description': _data[3]
                }
                last_id += 1

    return db, last_id


def get_file_name() -> str:
    return input("Введите имя файла: ")


def get_user_data() -> tuple:
    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    phone = input("Введите номер: ")
    description = input("Введите описание: ")

    return surname, name, phone, description


def get_surname() -> str:
    surname = input("Введите искомую фамилию: ")

    return surname


def get_confirm(message: str) -> bool:
    confirm = False
    while True:
        user_input = input(f"{message} (Y/N) > ")
        if user_input == 'Y':
            confirm = True
            break
        elif user_input == 'N':
            break

    return confirm


def print_data(db: dict) -> None:
    print("=" * 30)
    for _id, data in db.items():
        print(f"[{_id}: {data['surname']} | {data['name']} | {data['phone']}"
              f" | {data['description']} ]")


def print_record(db: dict, _id: int) -> None:
    if _id is not None:
        print_message(f'{db[_id]}')
    else:
        print_message("Запись не найдена!")


def print_message(message: str) -> None:
    print("=" * 30)
    print(f"{message}")


def print_menu() -> None:
    menu_points = [
        "Создать запись",
        "Вывести имеющиеся данные",
        "Экспортировть данные в файл",
        "Импортировать данные из файла",
        "Найти контакт",
        "Обновить данные контакта",
        "Удалить контакт",
        "Выход",
    ]
    print("\nВозможные действия:")
    print("=" * 30)
    for menu_point_num, menu_line in enumerate(menu_points):
        print(f"{menu_point_num + 1}. {menu_line}")

    print()


def menu(db: dict, last_id: int) -> None:
    while True:
        print_menu()
        user_input = input("Введите действие > ")

        if user_input == "1":
            record = get_user_data()
            db, last_id = create(db, last_id, *record)
        elif user_input == "2":
            print_data(db)
        elif user_input == "3":
            export_db(db, get_file_name())
        elif user_input == "4":
            db, last_id = import_db(db, last_id, get_file_name())
        elif user_input == "5":
            found_id = read(db, get_surname())
            print_record(db, found_id)
        elif user_input == "6":
            found_id = read(db, get_surname())
            update(db, found_id)
        elif user_input == "7":
            found_id = read(db, get_surname())
            delete(db, found_id)
        else:
            break


menu(phonebook, phonebook_last_id)
