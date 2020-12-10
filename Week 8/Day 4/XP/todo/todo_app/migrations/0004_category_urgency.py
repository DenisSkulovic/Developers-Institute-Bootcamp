# Generated by Django 3.1.4 on 2020-12-09 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0003_auto_20201209_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='urgency',
            field=models.CharField(choices=[(1, 'SUPER URGENT'), (2, 'URGENT'), (3, 'SORTA URGENT'), (4, 'NOT URGENT'), (5, 'CHILL')], default=3, max_length=100),
        ),
    ]
