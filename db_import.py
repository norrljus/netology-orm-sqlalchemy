import json
import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker
from models import create_tables, Publisher, Shop, Book, Stock, Sale

if __name__ == "__main__":
    username = 'postgres'
    password = '1111'
    port = '5432'
    dbname = 'bookstore'

    engine = sq.create_engine(f'postgresql://{username}:{password}@localhost:{port}/{dbname}')
    create_tables(engine)
    Session = sessionmaker(bind=engine)

    session = Session()

    with open('tests_data.json', 'r') as file:
        data = json.load(file)

    for x in data:
        model = {
            'publisher': Publisher,
            'shop': Shop,
            'book': Book,
            'stock': Stock,
            'sale': Sale
        }[x.get('model')]
        session.add(model(id=x.get('pk'), **x.get('fields')))
    session.commit()
    session.close()
