import os.path
import sqlite3


class CharField:
    def __init__(self, min_length=2, max_length=140):
        self.min_length = min_length
        self.max_length = max_length

    def set(self, st: str):
        if type(st) == str:
            self.char_field = st
        else:
            raise TypeError("это поле должно быть строкой")


class IntegerField:
    def __init__(self, min_value=0):
        self.min_value = min_value


class DataBase:
    def __init__(self, db_name=None):
        f = 0
        if db_name is None:
            self.connect_db = sqlite3.connect(':memory:')
        else:
            if os.path.exists(f'{db_name}'):
                f = 1
            self.connect_db = sqlite3.connect(f'{db_name}')
        self.coursor_db = self.connect_db.cursor()
        if not (db_name is not None and f == 1):
            self.coursor_db.execute(
                """
                CREATE TABLE advert
                (title_1  text PRIMARY KEY, price int)
                """
                )
            self.connect_db.commit()

    def insert(self, title=None, price=0):
        try:
            self.coursor_db.execute(f'INSERT INTO advert VALUES {title, price}')
            self.connect_db.commit()
        except sqlite3.DatabaseError as err:
            print('Error:', err)

    def count(self):
        self.coursor_db.execute('SELECT count() FROM advert')
        return self.coursor_db.fetchall()[0][0]
