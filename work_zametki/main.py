import data
import functions


if __name__ == '__main__':
    data.db.init_db()
    while True:

        user_mode: int = input(data.config.get_json_text()[0]['main_menu'])
        if user_mode.isdigit() and 0 < int(user_mode) < 5:
            print(
                "Вы выбрали режим: ",
                data.config.get_json_text()[1]['menu'][str(user_mode)],
                "\n\n"
            )

            if user_mode == "1":
                all_notes: list = data.db.show_note()

                result: str = functions.checks.create_text(all_notes)
                print(result)

            elif user_mode == "2":
                value = input("Введите ключевое слово:\n\n")
                notes_by_keyword = data.db.show_note_by_keyword(value)
                print('\n\n')
                print(notes_by_keyword)

            elif user_mode == "3":
                name_note: str = input("Введите название заметки:\n\n")
                value_note: str = input("Введите содержание заметки:\n\n")
                result: bool = data.db.add_note(name_note, value_note)
                print("Заметка сохранена!\n\n")
                if not result:
                    print("Вы пытаетесь добавить не string!\n\n")

            elif user_mode == "4":
                note_id: int = input("Введите ID заметки для удаления:\n\n")
                if not note_id.isdigit():
                    print("Нужно вводить число!\n\n")
                    continue
                result_delete: bool = data.db.delete_note(note_id)
                if result_delete:
                    print("Заметка удалена")
        else:
            print(
                "Ошибка, возможно вы ввели"
                "недопустимое число или вовсе не число\n\n"
            )
