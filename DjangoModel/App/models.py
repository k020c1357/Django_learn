from django.db import models

# Create your models here.
from django.db import models


class Person(models.Model):
    p_name = models.CharField(max_length=16, unique=True)
    p_age = models.IntegerField(default=18,db_column='age')

    # False = male,True=female
    p_sex = models.BooleanField(default=False, db_column='sex')

    class Meta:
        db_table = 'People'
