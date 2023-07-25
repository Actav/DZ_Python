# note.py

import json
import datetime

def add_note():
    title = input("Введите заголовок заметки: ")
    msg = input("Введите тело заметки: ")
    note = {
        "id": len(notes) + 1,
        "title": title,
        "msg": msg,
        "timestamp": str(datetime.datetime.now())
    }
    notes.append(note)
    save_notes()

def save_notes():
    with open("notes.json", "w") as f:
        json.dump(notes, f)

def read_notes(filter_date=None):
    with open("notes.json", "r") as f:
        notes_data = json.load(f)

    if filter_date:
        notes_data = [note for note in notes_data if note["timestamp"].startswith(filter_date)]

    return notes_data

def edit_note(note_id):
    title = input("Введите новый заголовок заметки: ")
    msg = input("Введите новое тело заметки: ")
    for note in notes:
        if note["id"] == note_id:
            note["title"] = title
            note["msg"] = msg
            note["timestamp"] = str(datetime.datetime.now())
            save_notes()
            return True
    return False

def delete_note(note_id):
    global notes
    notes = [note for note in notes if note["id"] != note_id]
    save_notes()

if __name__ == "__main__":
    notes = []

    try:
        with open("notes.json", "r") as f:
            notes = json.load(f)
    except FileNotFoundError:
        pass

    while True:
        print("\nВведите команду:")
        print("1. add - добавить заметку")
        print("2. read - прочитать список заметок")
        print("3. edit - редактировать заметку")
        print("4. delete - удалить заметку")
        print("0. exit - выйти из программы")

        command = input()

        if command == "add":
            add_note()
            print("Заметка успешно сохранена.")
        elif command == "read":
            filter_date = input("Введите дату для фильтрации заметок (или нажмите Enter для вывода всех заметок): ")
            notes_data = read_notes(filter_date)
            for note in notes_data:
                print(f"ID: {note['id']}, Title: {note['title']}, Body: {note['msg']}, Timestamp: {note['timestamp']}")
        elif command == "edit":
            note_id = int(input("Введите ID заметки, которую хотите отредактировать: "))
            if edit_note(note_id):
                print("Заметка успешно отредактирована.")
            else:
                print("Заметка не найдена.")
        elif command == "delete":
            note_id = int(input("Введите ID заметки, которую хотите удалить: "))
            delete_note(note_id)
            print("Заметка успешно удалена.")
        elif command == "exit":
            break
        else:
            print("Неверная команда. Пожалуйста, повторите ввод.")
