#!/usr/bin/env python3
"""
Запуск виноградной базы данных
"""

import os
import sys

# Запускаем напрямую
if __name__ == '__main__':
    # Проверяем, что app.py существует
    if not os.path.exists('app.py'):
        print("❌ Ошибка: файл app.py не найден!")
        sys.exit(1)

    # Добавляем текущую папку в путь Python
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

    # Импортируем и запускаем
    try:
        from app import app, create_structure, init_database

        print("=" * 70)
        print("🍇 ВИНОГРАДНАЯ БАЗА ДАННЫХ")
        print("=" * 70)

        # Создаем структуру
        create_structure()

        # Инициализируем БД
        init_database()

        print("🚀 Запуск сервера...")
        print("📁 База данных: grape_database.db")
        print("🌐 URL: http://localhost:5000")
        print("👤 Пользователь: http://localhost:5000/user")
        print("👑 Админ: http://localhost:5000/admin")
        print("🔐 Логин админа: admin / admin123")
        print("=" * 70)

        # Запускаем Flask
        app.run(
            debug=True,
            host='0.0.0.0',
            port=5000,
            threaded=True
        )

    except ImportError as e:
        print(f"❌ Ошибка импорта: {e}")
        sys.exit(1)
