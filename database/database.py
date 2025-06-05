from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

engine = create_engine('postgresql+psycopg2://postgres:12345@localhost:5432/pomodoro_db')

Session = sessionmaker(engine)
def get_db_session() -> Session:
    return Session()
