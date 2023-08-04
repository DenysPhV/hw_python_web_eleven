from dotenv import dotenv_values


class Config:
    # config = dotenv_values(".env")
    # DB_URL = config.get("DATABASE_URL")
    # DB_URL = "postgresql://postgres:secret@127.0.0.1:5432/todo_db"
    DB_URL = "posgresql+asyncpg://postgres:58796@localhost/todo_db"


config = Config
