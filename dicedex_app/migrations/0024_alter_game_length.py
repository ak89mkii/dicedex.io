# Generated by Django 3.2.8 on 2022-09-05 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dicedex_app', '0023_game_gundam_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='length',
            field=models.IntegerField(max_length=100),
        ),
    ]
