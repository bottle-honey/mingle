# Generated by Django 3.2.13 on 2022-06-23 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0002_auto_20220624_0305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='class_id',
            field=models.TimeField(primary_key=True, serialize=False),
        ),
    ]
