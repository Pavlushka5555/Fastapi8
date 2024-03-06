# tests/conftest.py
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Base
from db.session import SessionLocal, engine

@pytest.fixture(scope="session")
def db():
    Base.metadata.create_all(bind=engine)
    yield engine
    Base.metadata.drop_all(bind=engine)

@pytest.fixture
def session(db):
    connection = db.connect()
    transaction = connection.begin()
    session = sessionmaker(autocommit=False, autoflush=False, bind=connection)()
    yield session
    session.close()
    transaction.rollback()
    connection.close()
