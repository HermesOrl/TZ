import sqlite3
import functions


def current_connection(func):
    def decorator(*args, **kwargs):
        with sqlite3.connect('database.db') as conn:
            result = func(conn, *args, **kwargs)
        return result

    return decorator


@current_connection
def init_db(conn):
    """
    Создаем таблицу в ранее инициализируемой базе данных.

        Параметры:
            conn: Наше подключение к базе

        Возвращаемое значение:
            Отсутствует
    """

    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS notes (
                id_note                     INTEGER PRIMARY KEY AUTOINCREMENT,
                header                      INTEGER,
                content                     STRING);
            """)
    conn.commit()


@current_connection
def add_note(conn, header: str, content: str) -> bool:
    """
    Добавляем новую заметку в таблицу notes.

        Параметры:
            conn: Наше подключение к базе
            header: Заголовок заметки
            content: Содержание заметки

        Возвращаемое значение:
            True, False
    """

    # Проверка на string
    result_check: bool = functions.checks.check_string(header, content)
    if not result_check:
        return False

    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO notes VALUES(NULL, '{header}', '{content}')")
    conn.commit()

    return True


@current_connection
def show_note(conn) -> list:
    """
    Показываем все заметки.

        Параметры:
            conn: Наше подключение к базе

        Возвращаемое значение:
            all_notes: Все заметки
    """

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM notes")
    all_notes: list = cursor.fetchall()

    return all_notes


def show_note_by_keyword(keyword: str) -> str:
    """
    Ищем заметку по ключевому слову.
    Будем искать везде - в заголовках и в содержании заметки.
    Мы будем сначала получать все заметки, а далее уже фильтровать.

        Параметры:
           keyword: Ключевое слово

        Возвращаемое значение:
            notes_by_key: Найденные заметки
    """

    # Получаем все заметки из прошлой функции
    all_notes: list = show_note()
    notes_by_key: str = functions.checks.check_value(keyword, all_notes)

    return notes_by_key


@current_connection
def delete_note(conn, note_id: int) -> bool:
    """
    Удаляем заметку по id.

        Параметры:
            conn: Наше подключение к базе
            id_note: id заметки

        Возвращаемое значение:
            True в случае успеха
    """

    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM notes WHERE id_note = {note_id}")
    conn.commit()

    return True


