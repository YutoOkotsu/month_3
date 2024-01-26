import sqlite3
from pathlib import Path


def init_db():
    """
    Создается соединение с БД и курсор
    """
    global db, cursor
    db = sqlite3.connect(
        Path(__file__).parent.parent / "db.sqlite"
    )
    cursor = db.cursor()

def create_tables():
    cursor.execute("""
        --sql
        DROP TABLE IF EXISTS product;
    """)
    cursor.execute("""
        --sql
        DROP TABLE IF EXISTS cats;
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cats (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        );
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS product (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price INTEGER,
            cat INTEGER,
            FOREIGN KEY (cat) REFERENCES cats (id)
        );
    """)
    db.commit()

def populate_db():
    """
    Заполнение таблиц
    """
    cursor.execute("""
        --sql
        INSERT INTO cats (name) VALUES
            ('Books'),
            ('Comics'),
            ('Manga')
        """)
    cursor.execute("""
        INSERT INTO product (name, price, cat) VALUES
            ('Хитрый как лис, Ловкий как тигр', 1200, 1),
            ('Война и мир', 400, 1),
            ('Dead Pull', 900, 2),
            ('Batman', 900, 2),
            ('What if', 1200, 2),
            ('Spider-Man', 1200, 2),
            ('Jujutsu Kaisen', 650, 3),
            ('One piece', 850, 3),
            ('Naruto', 650, 3),
            ('The Daily Life of the Immortal King', 550, 3)
        """
    )
    db.commit()

def get_products():

    cursor.execute("""
        SELECT * FROM product
    """)
    return cursor.fetchall()

def get_product(id):
    cursor.execute("""
        SELECT * FROM product WHERE id= :cid
    """, {"cid": id})
    return cursor.fetchone()

def get_products_by_cat(id):
    cursor.execute("""
        SELECT * FROM product WHERE cat = :cid
    """, {"cid": id})
    return cursor.fetchall()

if __name__ == '__main__':
    init_db()
    # populate_db()
    create_tables()
    print(get_products_by_cat(3))