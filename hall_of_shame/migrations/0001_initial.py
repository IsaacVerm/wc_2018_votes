# Generated by Django 2.0.2 on 2018-05-07 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('score', models.IntegerField(default=0)),
                ('paid', models.BooleanField(default=False)),
                ('times_cheated', models.IntegerField(default=0)),
            ],
        ),
    ]
