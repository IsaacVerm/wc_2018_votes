# Generated by Django 2.0.2 on 2018-05-08 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0006_auto_20180507_1545'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='score',
            name='game',
        ),
        migrations.RemoveField(
            model_name='score',
            name='user',
        ),
    ]