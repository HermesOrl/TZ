"""
Импорт нужных функций

database.py Содержит инструменты для работы с базой данных

Используется для main.py
"""

from .database import init_db, add_note, show_note, \
    show_note_by_keyword, delete_note
