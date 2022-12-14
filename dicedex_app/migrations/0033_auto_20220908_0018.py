# Generated by Django 3.2.8 on 2022-09-08 00:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dicedex_app', '0032_auto_20220907_2327'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='theme',
            name='color',
            field=models.CharField(choices=[('Dark', 'Dark'), ('Light', 'Light')], default='Light', max_length=30),
        ),
    ]
