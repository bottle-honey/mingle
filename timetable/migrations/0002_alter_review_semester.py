# Generated by Django 3.2.13 on 2022-06-29 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='semester',
            field=models.CharField(choices=[('1', '21-1'), ('2', '21-2'), ('3', '22-1')], default='22-1', max_length=4),
        ),
    ]
