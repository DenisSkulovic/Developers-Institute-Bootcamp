# Generated by Django 3.1.4 on 2020-12-22 14:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mainpage', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('type', models.CharField(choices=[('Sell', 'Sell'), ('Buy', 'Buy')], max_length=5)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainpage.card')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
