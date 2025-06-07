# clear_alembic_version.py
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os
load_dotenv()
DATABASE_URL = os.getenv("DBSECRETURL")
engine = create_engine(DATABASE_URL)

with engine.connect() as connection:
    connection.execute(text("TRUNCATE TABLE alembic_version;"))
    connection.commit()
    print("Таблица alembic_version очищена!")