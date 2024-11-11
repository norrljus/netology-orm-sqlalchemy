import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Publisher(Base):
    __tablename__ = "Publisher"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=50), nullable=False)


class Book(Base):
    __tablename__ = "Book"

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=50), nullable=False)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey("Publisher.id"), nullable=False)

    publisher = relationship(Publisher, backref="books")


class Shop(Base):
    __tablename__ = "Shop"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=30), nullable=False)


class Stock(Base):
    __tablename__ = "Stock"

    id = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey("Book.id"), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey("Shop.id"), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)

    book = relationship(Book, backref="stocks")
    shop = relationship(Shop, backref="shops")


class Sale(Base):
    __tablename__ = "Sale"

    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Float, nullable=False)
    date_sale = sq.Column(sq.DateTime, nullable=False)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey("Stock.id"), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)

    stock = relationship(Stock, backref="sales")


def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
