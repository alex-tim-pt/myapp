import peewee as pw

db = pw.SqliteDatabase('mydb.db')

class baseModel(pw.Model):
   class Meta:
       abstract = True
       database = db

class Employee(baseModel):
    first_name = pw.CharField(max_length=100)
    last_name = pw.CharField(max_length=100)
    position = pw.CharField()

