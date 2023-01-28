import sqlite3

def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
        return conn
    except sqlite3.Error as e:
        print(e)

def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)

def create_product(conn, product: tuple):
    try:
        sql = '''INSERT INTO products
        (product_title, price, quantity)
        VALUES (?, ?, ?)'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)
        
database = 'hw.db'
sql_create_products_table = '''
CREATE TABLE products   (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR (200) NOT NULL,
price DOUBLE (10, 2) NOT NULL DEFAULT 0.0,
quantity INTEGER (5) NOT NULL DEFAULT 0
)
'''

connection = create_connection(database)
if connection is not None:
    print('Connected succesfully')

    create_product(connection, ('Кефир', 58.80, 7))
    create_product(connection, ('Мороженое: Бахрома', 60.53, 30))
    create_product(connection, ('Пепси 2л', 180.00, 4))
    create_product(connection, ('NITRO', 90.40, 12))
    create_product(connection, ('Контик', 50.90, 5))
    create_product(connection, ('Жидкое мыло с запахом ванили', 67.89, 2))
    create_product(connection, ('Мыло детское', 108.60, 7))
    create_product(connection, ('Кириешки Flint', 26.12, 20))
    create_product(connection, ('Семечки Джин', 59.99, 6))
    create_product(connection, ('Гамбургер "Тойбосс"', 200.00, 3))
    create_product(connection, ('Alpen Gold', 114.59, 4))
    create_product(connection, ('Шампунь', 333.00, 14))
    create_product(connection, ('Сливочное Масло', 150.00, 5))
    create_product(connection, ('Масло 3 желание', 200.00, 12))
    create_product(connection, ('Детское-лечебное Масло', 400.00, 2))


def update_product_quantity(conn, product: tuple):
    try:
        sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def update_product_price(conn, product: tuple):
    try:
        sql = '''UPDATE products SET price = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def delete_product_by_id(conn, id: int):
    try:
        sql = '''DELETE FROM products WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def print_all_products(conn):
    try:
        sql = '''SELECT * FROM products'''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)



def print_all_products_by_price_and_quntity(conn):
    try:
        sql = '''SELECT * FROM products WHERE price < 100.0 AND quantity > 5'''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


def search_by_word(conn, word):
    try:
        sql = '''SELECT * FROM products WHERE product_title LIKE ?'''
        cursor = conn.cursor()
        cursor.execute(sql, ('%' + word + '%',))

        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


    create_product(connection)
    create_table(connection, sql_create_products_table)
    print_all_products_by_price_and_quntity(connection)
    search_by_word(connection, 'мыло')
    connection.close()
    print("Done")
    
    

