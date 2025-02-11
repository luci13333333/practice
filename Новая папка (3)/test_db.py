from config import Config
from sqlalchemy import create_engine

engine = create_engine(Config.DATABASE_URL)
connection = engine.connect()
print("Подключение успешно установлено!")