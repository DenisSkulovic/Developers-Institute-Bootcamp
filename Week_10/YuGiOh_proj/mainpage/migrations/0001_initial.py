# Generated by Django 3.1.4 on 2020-12-22 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Archetype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2550)),
            ],
        ),
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2550)),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_id', models.IntegerField()),
                ('name', models.CharField(max_length=2550)),
                ('desc', models.CharField(max_length=2550, null=True)),
                ('card_atk', models.IntegerField(blank=True, null=True)),
                ('card_def', models.IntegerField(blank=True, null=True)),
                ('card_level', models.IntegerField(blank=True, null=True)),
                ('archetype', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainpage.archetype')),
                ('attribute', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainpage.attribute')),
            ],
        ),
        migrations.CreateModel(
            name='Cardset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('set_name', models.CharField(max_length=2550)),
                ('set_code', models.CharField(max_length=2550)),
                ('set_rarity', models.CharField(max_length=2550)),
                ('set_rarity_code', models.CharField(max_length=2550)),
                ('set_price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_id', models.IntegerField()),
                ('image_url', models.URLField()),
                ('image_url_small', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2550)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2550)),
            ],
        ),
        migrations.CreateModel(
            name='CardPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardmarket_price', models.FloatField()),
                ('tcgplayer_price', models.FloatField()),
                ('ebay_price', models.FloatField()),
                ('amazon_price', models.FloatField()),
                ('coolstuffinc_price', models.FloatField()),
                ('card', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainpage.card')),
            ],
        ),
        migrations.AddField(
            model_name='card',
            name='cardset',
            field=models.ManyToManyField(blank=True, to='mainpage.Cardset'),
        ),
        migrations.AddField(
            model_name='card',
            name='image',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainpage.image'),
        ),
        migrations.AddField(
            model_name='card',
            name='race',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainpage.race'),
        ),
        migrations.AddField(
            model_name='card',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainpage.type'),
        ),
    ]
