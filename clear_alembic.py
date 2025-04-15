# clear_alembic_version.py
from sqlalchemy import create_engine, text

DATABASE_URL = "postgresql+psycopg2://postgres:dfdfdfdjk34@localhost/apifirst"
engine = create_engine(DATABASE_URL)

with engine.connect() as connection:
    # Оберните запрос в text()!
    connection.execute(text("TRUNCATE TABLE alembic_version;"))
    connection.commit()  # Явное подтверждение изменений
    print("Таблица alembic_version очищена!")