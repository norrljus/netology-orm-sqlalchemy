import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker
from models import Publisher, Shop, Book, Stock, Sale
from tabulate import tabulate


def publisher_query():
    avpub = []
    for w in session.query(Publisher.name).all():
        avpub.append(w[0])
    print(f"Available publishers: {', '.join(avpub)}. ('q' to exit)")
    while True:
        pubq = input("Input publisher: ")
        if pubq == "q":
            break
        elif pubq in avpub:
            for q in (session.query(Sale).join(Publisher.books)
                                         .join(Book.stocks)
                                         .join(Stock.shop)
                                         .join(Stock.sales).filter(Publisher.name == pubq).all()):
                print(f"{q.stock.book.title} | {q.stock.shop.name} | {q.price} | {str(q.date_sale)[:10]}")
        else:
            print("Error!")


if __name__ == "__main__":
    username = 'postgres'
    password = '1111'
    port = '5432'
    dbname = 'bookstore'

    engine = sq.create_engine(f'postgresql://{username}:{password}@localhost:{port}/{dbname}')
    Session = sessionmaker(bind=engine)
    session = Session()

    publisher_query()

    session.close()
