import peewee as pw


db = pw.PostgresqlDatabase(
    database='dfgdtl6jp8m736',
    user='swutriiwpeabfn',
    password='a308d1808ddb61a6deedb1dbd60432763a9365974f12710c75f3ade0094bea98',
    host='ec2-3-248-103-75.eu-west-1.compute.amazonaws.com',
    port=5432
)


class baseModel(pw.Model):
   class Meta:
       abstract = True
       database = db

class Employee(baseModel):
    first_name = pw.CharField(max_length=100)
    last_name = pw.CharField(max_length=100)
    position = pw.CharField()

