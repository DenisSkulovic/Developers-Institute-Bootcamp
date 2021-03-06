# Generated by Django 3.1.4 on 2020-12-09 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0002_auto_20201209_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='category',
            field=models.ManyToManyField(to='todo_app.Category'),
        ),
        migrations.RemoveField(
            model_name='category',
            name='name',
        ),
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(default='default', max_length=100, unique=True),
        ),
    ]
