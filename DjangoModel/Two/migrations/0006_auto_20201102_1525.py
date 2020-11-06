# Generated by Django 3.1.2 on 2020-11-02 06:25

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('Two', '0005_animal'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='animal',
            managers=[
                ('a_m', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='animal',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
    ]