# config.example.py
# Копируйте этот файл в config.py и настройте свои значения

SECRET_KEY = 'change-this-in-production'
DATABASE_PATH = 'grape_database.db'

# Email настройки
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = 'your-email@gmail.com'
MAIL_PASSWORD = 'your-app-password'
MAIL_DEFAULT_SENDER = 'your-email@gmail.com'

# Админ доступ
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'admin123'

# Папки
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB