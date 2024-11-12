import json
from models import Publisher, Shop, Book, Stock, Sale
import db_connect

if __name__ == "__main__":
    session = db_connect.make_session()

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
