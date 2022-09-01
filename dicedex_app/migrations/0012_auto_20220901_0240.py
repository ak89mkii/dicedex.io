# Generated by Django 3.2.8 on 2022-09-01 02:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dicedex_app', '0011_alter_game_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='owner',
            field=models.CharField(default='1', max_length=100),
        ),
        migrations.AlterField(
            model_name='game',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
