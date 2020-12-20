# Generated by Django 3.1.4 on 2020-12-16 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trading', '0004_auto_20201216_1758'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2550)),
            ],
        ),
        migrations.AddField(
            model_name='card',
            name='card_atk',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='card_def',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='card_level',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='archetype',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='trading.archetype'),
        ),
        migrations.AlterField(
            model_name='card',
            name='cardset',
            field=models.ManyToManyField(null=True, to='trading.Cardset'),
        ),
        migrations.AlterField(
            model_name='card',
            name='desc',
            field=models.CharField(max_length=2550, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='race',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='trading.race'),
        ),
        migrations.AlterField(
            model_name='card',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='trading.type'),
        ),
        migrations.AddField(
            model_name='card',
            name='attribute',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='trading.attribute'),
        ),
    ]
