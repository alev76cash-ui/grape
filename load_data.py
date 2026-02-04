import sqlite3
import csv
import os

DATABASE = 'grape_database.db'
CSV_FILE = 'grape_varieties.csv'

def load_data():
    print("Загрузка данных из CSV в базу данных...")
    
    # Удаляем старую базу данных
    if os.path.exists(DATABASE):
        os.remove(DATABASE)
        print("✅ Удалена старая база данных")
    
    # Создаем новое подключение
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    # Создаем таблицу
    cursor.execute('''
        CREATE TABLE grape_varieties (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            purpose TEXT,
            ripening_period TEXT,
            frost_resistance TEXT,
            berry_color TEXT,
            taste TEXT,
            sugar_content TEXT,
            acidity TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Загружаем данные из CSV
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            imported = 0
            
            for row in reader:
                try:
                    # Пробуем получить ID
                    row_id = row.get('ID')
                    if not row_id:
                        continue
                    
                    # Вставляем данные
                    cursor.execute('''
                        INSERT INTO grape_varieties
                        (id, name, purpose, ripening_period, frost_resistance,
                         berry_color, taste, sugar_content, acidity)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ''', (
                        int(row_id),
                        row.get('Название', '').strip(),
                        row.get('Назначение', '').strip(),
                        row.get('Срок созревания', '').strip(),
                        row.get('Морозостойкость', '').strip(),
                        row.get('Цвет ягод', '').strip(),
                        row.get('Вкус', '').strip(),
                        row.get('Сахар', '').strip(),
                        row.get('Кислотность', '').strip()
                    ))
                    imported += 1
                    
                except Exception as e:
                    print(f"Ошибка при импорте строки: {e}")
        
        print(f"✅ Импортировано {imported} сортов")
    else:
        print(f"❌ Файл {CSV_FILE} не найден")
    
    conn.commit()
    conn.close()
    print("✅ Данные успешно загружены")

if __name__ == '__main__':
    load_data()