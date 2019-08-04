import peewee

DATABASE = r'gerenciamentoLogin.db'

db = peewee.SqliteDatabase(DATABASE)

def createTables():
    try:
        with db:
            db.create_tables([User])
    except Exception as e:
        print(e.__str__())

class BaseModel(peewee.Model):
    class Meta:
        database = db

class User(BaseModel):
    username = peewee.CharField()
    password = peewee.CharField()
    email = peewee.CharField(unique=True)
    entrou_em = peewee.DateTimeField()
