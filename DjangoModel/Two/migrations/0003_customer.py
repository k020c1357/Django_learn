# Generated by Django 3.1.2 on 2020-11-01 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Two', '0002_grade_order_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=16)),
                ('c_cost', models.IntegerField(default=10)),
            ],
        ),
    ]