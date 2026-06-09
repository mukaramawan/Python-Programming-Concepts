from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# SQLALCHEMY_DATABASE_URL = "sqlite:///./todosapp.db"

# pip install psycopg2-binary
# psycopg2-binary is a pre-compiled version of the Psycopg2 library used to connect Python applications to a PostgreSQL database.

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:mukaram@localhost/todoapplicationdatabase"


# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
                                    # Required for SQLite to connect from only one thread

engine = create_engine(SQLALCHEMY_DATABASE_URL)

session_local = sessionmaker(autoflush=False, autocommit=False, bind=engine)
                                    # autoflush=False means not to flush changes to the database automatically. (temp)
                                    # autocommit=False means not to save changes to the database automatically. (permanent)
base = declarative_base()