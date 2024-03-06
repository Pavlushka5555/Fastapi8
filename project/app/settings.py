from dotenv import load_dotenv
import os

# Загрузка переменных окружения из файла .env
load_dotenv()

class Settings:
    app_name: str = "Test API"
    
    DATABASE_URL: str
    POSTGRES_DATABASE_URLS: str
    POSTGRES_DATABASE_URLA: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str
    POSTGRES_DB: str

    # Чтение переменных окружения из файла .env
    POSTGRES_PORT = os.environ.get('POSTGRES_PORT')
    POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
    POSTGRES_USER = os.environ.get('POSTGRES_USER')
    POSTGRES_DB = os.environ.get('POSTGRES_DB')
    POSTGRES_HOST = os.environ.get('POSTGRES_HOST')
    POSTGRES_DATABASE_URLA = f"postgresql+asyncpg://" \
                              f"{POSTGRES_USER}:{POSTGRES_PASSWORD}" \
                              f"@{POSTGRES_HOST}:{POSTGRES_PORT}" \
                              f"/{POSTGRES_DB}"
    POSTGRES_DATABASE_URLS = f"postgresql://" \
                              f"{POSTGRES_USER}:{POSTGRES_PASSWORD}" \
                              f"@{POSTGRES_HOST}:{POSTGRES_PORT}" \
                              f"/{POSTGRES_DB}"

    TPOSTGRES_PORT = os.environ.get('TPOSTGRES_PORT')
    TPOSTGRES_PASSWORD = os.environ.get('TPOSTGRES_PASSWORD')
    TPOSTGRES_USER = os.environ.get('TPOSTGRES_USER')
    TPOSTGRES_DB = os.environ.get('TPOSTGRES_DB')
    TPOSTGRES_HOST = os.environ.get('TPOSTGRES_HOST')
    POSTGRES_DATABASE_URLT = f"postgresql://" \
                              f"{TPOSTGRES_USER}:{TPOSTGRES_PASSWORD}" \
                              f"@{TPOSTGRES_HOST}:{TPOSTGRES_PORT}" \
                              f"/{TPOSTGRES_DB}"
