# Generated by Django 2.0.2 on 2018-05-06 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='away_team',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='home_team',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='prediction',
            name='game',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='votes.Game'),
        ),
        migrations.AddField(
            model_name='prediction',
            name='goals_away_team',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='prediction',
            name='goals_home_team',
            field=models.IntegerField(null=True),
        ),
    ]