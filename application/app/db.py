from sqlalchemy import URL, create_engine

from queries import Queries

url = URL.create('postgresql',
    username='postgres',
    password='3ja6mz80q',
    host='localhost',
    database='postgres')

engine = create_engine(url)

db = Queries(engine.connect())