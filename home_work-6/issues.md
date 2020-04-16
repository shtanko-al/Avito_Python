# Total number of issues: 1

## issue-01
Напишите необходимые классы для реализации простой [ORM](https://ru.wikipedia.org/wiki/ORM)\
Требования к `ORM`:
* поддерживает два вида полей
    * `CharField`
    * `IntegerField`
* умеет работать только с [SQLite](https://docs.python.org/3/library/sqlite3.html)
* позволяет создавать таблицы
* позволяет сохранять объекты
* позваляет получать все записи из таблицы

Пример использования:
```python
from simple_orm import SqliteDatabase, Model, fields


db = SqliteDatabase(':memory:')


class BaseModel(Model):
    class Meta:
        database = db


class Advert(BaseModel):
    title = CharField(max_length=180)
    price = IntegerField(min_value=0)


db.connect()
db.create_tables([Advert])

Advert.create(title='iPhone X', price=100)
adverts = Advert.select()
assert str(adverts[0]) == 'iPhone X | 100 ₽'
```

*Подсказки*:
* можно посмотреть, как реализован [peewee](https://github.com/coleifer/peewee)
* презентация [Your own ORM in Python How and Why](https://speakerdeck.com/lig/your-own-orm-in-python-how-and-why)

**DoD (Definition of Done) - критерии, позволяющие понять, что задача сделана, как ожидается**:
* написан класс для работы с SQLite
* можно создать таблицы в БД из моделей
* у поля `CharField` проверяется, что значение является строкой и соответсвует параметрам `min_length` и `max_length`
* у поля `IntegerField` проверяется, что значение является числом и соответсвует параметру `min_value`
* можно добавлять записи в БД
* у класса модели нет атрибута `Meta`, но при объявление базовго класса `BaseModel` должен быть
* код из примера использования выполнятется в точности или очень близко
* можно создавать и сохранять любые другие модели
* как минимум 6 осмысленных тестов
* файл README.md с описанием шагов для запуска тестов к заданию
* файл result с командами и результатами запуска тестов к заданию
* нет замечаний от `flake8`
