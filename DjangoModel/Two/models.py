from django.db import models


# Create your models here.
class User(models.Model):
    u_name = models.CharField(max_length=16, unique=True)
    u_password = models.CharField(max_length=256)


class Order(models.Model):
    o_num = models.CharField(max_length=16, unique=True)
    o_time = models.DateField(auto_now_add=True)


class Grade(models.Model):
    s_name = models.CharField(max_length=16)


class Student(models.Model):
    s_name = models.CharField(max_length=16)
    s_grade = models.ForeignKey(Grade, on_delete=models.CASCADE)  # 新版 会报错的地方


class Customer(models.Model):
    c_name = models.CharField(max_length=16)
    c_cost = models.IntegerField(default=10)


class Company(models.Model):
    c_name = models.CharField(max_length=16)
    c_girl_num = models.IntegerField(default=5)
    c_boy_num = models.IntegerField(default=3)


class AnimalManager(models.Manager):
    # 自定义管理器
    def get_queryset(self):
        return super(AnimalManager, self).get_queryset().filter(is_delete=False)
    # 可进一步添加 方法


class Animal(models.Model):
    a_name = models.CharField(max_length=16)
    is_delete = models.BooleanField(default=False)

    # 使用自定义管理器
    # objects = AnimalManager()  好处： 增量添加代码 不更改原有代码
    a_m = AnimalManager()  # 显性 属性 ---之后系统不进行自动生成管理器
