# Generated by Django 2.0.2 on 2018-05-07 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hall_of_shame', '0002_remove_user_score'),
        ('votes', '0005_prediction_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='prediction',
            name='goals_away_team',
        ),
        migrations.RemoveField(
            model_name='prediction',
            name='goals_home_team',
        ),
        migrations.AddField(
            model_name='game',
            name='away_goals',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='home_goals',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='prediction',
            name='predicted_goals_away',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='prediction',
            name='predicted_goals_home',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hall_of_shame.User'),
        ),
        migrations.AddField(
            model_name='score',
            name='game',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='votes.Game'),
        ),
        migrations.AddField(
            model_name='score',
            name='prediction',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='votes.Prediction'),
        ),
        migrations.AddField(
            model_name='score',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hall_of_shame.User'),
        ),
    ]
