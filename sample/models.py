from django.db import models

# Create your models here.
class username(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=500)



    class meta:
      db_table='user_info'
    