# config.example.py
# Копируйте этот файл в config.py и настройте свои значения

# Настройки приложения
SECRET_KEY = 'ваш-секретный-ключ'
DATABASE = 'grape_database.db'

# Email настройки
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = 'ваш-email@gmail.com'
MAIL_PASSWORD = 'ваш-пароль'

# Админ доступ
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'admin123'

# Папки
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB