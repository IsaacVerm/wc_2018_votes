# Generated by Django 2.0.2 on 2018-05-06 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0003_game_round'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='date',
            field=models.DateTimeField(null=True),
        ),
    ]
