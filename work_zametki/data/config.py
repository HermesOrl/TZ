import json


def get_json_text() -> dict:

    """
    Получение json с текстами для приложения

        Возвращаемое значение:
            json_(list)

    """

    with open('data\\text.json', 'r', encoding='utf-8') as file_json:
        json_: dict = json.load(file_json)
        return json_
