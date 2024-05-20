# imports
from sqlmodel import create_engine, SQLModel, Session
from typing import Annotated
from fastapi import Depends


# db config
db_file_name = 'EconomedDB.db'
db_url = f'sqlite:///{db_file_name}'

connection_args = {'check_same_thread': False}
Engine = create_engine(db_url, connect_args=connection_args)


# connect / create / db or table
def init_Database():
    SQLModel.metadata.create_all(Engine)
    print('Database Connected! ✅')



def get_Session():
    with Session(Engine) as session:
        yield session


Database = Annotated[Session, Depends(get_Session)]