# Generated by Django 3.2.6 on 2021-08-19 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actor',
            field=models.ManyToManyField(related_name='actor1', to='movies.Actor'),
        ),
    ]
