
def check_string(header_line, content_line):
    """
    Проверка на string

        Параметры:
            header_line: Заголовок заметки
            content_line: Содержание заметки

        Возвращаемое значение:
            True, False
    """
    if isinstance(header_line, str) or isinstance(content_line, str):
        return False

    return True


def check_value(value, content):
    """
    Проверка на наличия строк в базе.
    Фильтрация и создание красивого текста

        Параметры:
            value: Ключевое слово
            content Исходные данные

        Возвращаемое значение:
            found_notes_txt: Отфильтрованный текст
    """
    found_notes_array = []
    found_notes_txt = ""
    for note in content:

        if value.lower() in str(note[1]).lower()\
                or value.lower() in str(note[2]).lower():
            found_notes_array.append([note[0], note[1], note[2]])
    for note in found_notes_array:
        found_notes_txt += f"      {note[1]}               ID: {note[0]}" \
                           f"\n\n{note[2]}\n\n" \
                           f"__________________________________\n\n"
    return found_notes_txt


def create_text(value):
    """
    Создание красивого текста для вывода в консоль

        Параметры:
            value: Исходные данные

        Возвращаемое значение:
            text_: Отфильтрованный текст
    """
    text_ = ""
    for line in value:
        text_ += f"     {line[1]}" \
                 f"               ID: {line[0]}" \
                 f"\n\n{line[2]}" \
                 f"\n\n__________________________________\n\n"
    return text_
