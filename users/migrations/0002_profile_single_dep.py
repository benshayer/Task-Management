# Generated by Django 3.1 on 2020-08-31 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='single_dep',
            field=models.CharField(default='Soldier', max_length=100),
        ),
    ]
