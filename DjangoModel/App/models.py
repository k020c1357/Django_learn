from django.db import models

# Create your models here.
from django.db import models


class Person(models.Model):  # query set（查询集） 创建可迭代的对象 object
    p_name = models.CharField(max_length=16, unique=True)
    p_age = models.IntegerField(default=18, db_column='age')

    # False = male,True=female
    p_sex = models.BooleanField(default=False, db_column='sex')
    p_hobby = models.CharField(max_length=32, null=True, blank=True)

    @classmethod
    def create(cls, p_name, p_age=100, p_sex=True, p_hobby='hiking'):  # 增加 类方法 （函数） 不需要 重新 迁移
        return cls(p_name=p_name, p_age=p_age, p_sex=p_sex, p_hobby=p_hobby)

    class Meta:
        db_table = 'People'
