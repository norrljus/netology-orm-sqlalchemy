from models import Publisher, Book, Stock, Sale
import db_connect


def publisher_query():
    avpub = []
    for w in session.query(Publisher.id, Publisher.name).all():
        avpub.append(f"{w[0]}: {w[1]}")
    print(f"Available publishers: {', '.join(avpub)}. ('q' to exit)")
    while True:
        pubq = input("Input publisher's name or id: ")
        query1 = (session.query(Sale).join(Publisher.books)
                  .join(Book.stocks)
                  .join(Stock.shop)
                  .join(Stock.sales))
        if pubq == "q":
            break
        elif pubq.isdigit():
            for q in (query1.filter(Publisher.id == pubq).all()):
                print(
                    f"{q.stock.book.title: <40} | {q.stock.shop.name: <10} | "
                    f"{q.price: <8} | {q.date_sale.strftime('%d-%m-%Y')}")
        else:
            for q in (query1.filter(Publisher.name == pubq).all()):
                print(
                    f"{q.stock.book.title: <40} | {q.stock.shop.name: <10} | "
                    f"{q.price: <8} | {q.date_sale.strftime('%d-%m-%Y')}")


if __name__ == "__main__":
    session = db_connect.make_session()
    publisher_query()
    session.close()
