from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# connect SQLITE database
SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosapp.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args = {'check_same_thread' : False})


# Connect PostgreSQL database
'''
SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:localhost@localhost/TodoApplicationDatabase'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
'''

# Connect MySQL database
'''
SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:localhost@127.0.0.1:3306/todoapplicationdatabase'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
'''
sessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

Base = declarative_base()

