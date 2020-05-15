from home_work-6.simple_orm import DataBase

vv = ['iphon', 7500]
v1 = ['adfg', 33]
v2 = ['agastrhdfg', 323453]
v3 = ['gjd', 234]
# print(str(vv))

db = DataBase()
db.insert(title='sphfgjon',
          price=7500
          )
db.insert(title='dfghjdg',
          price=245
          )
db.insert(title='arthsrt',
          price=2456
          )
db.insert(title='xftus',
          price=4567
          )
db.insert(title='sphfgjon',
          price=7500
          )
db.insert(title='kdtyujdt',
          price=7500
          )
print('количество записей в ', db.count())
print(db.__class__.__name__)
