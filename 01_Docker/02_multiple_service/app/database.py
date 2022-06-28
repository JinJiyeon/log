from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# 보안 강화하려면 dotenv 활용해야 함
db_info = {
    "user": os.environ['MYSQL_USER'],
    "password": os.environ['MYSQL_USER_PASSWORD'],
    "host": os.environ['MYSQL_HOST'],
    "database": os.environ['MYSQL_DATABASE']
}

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{db_info['user']}:{db_info['password']}@{db_info['host']}/{db_info['database']}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
