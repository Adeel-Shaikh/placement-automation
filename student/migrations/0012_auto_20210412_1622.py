# Generated by Django 3.1.7 on 2021-04-12 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0011_projectlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectlist',
            name='Semester',
            field=models.CharField(choices=[('1', 'I'), ('2', 'II'), ('3', 'III'), ('4', 'IV'), ('5', 'V'), ('6', 'VI'), ('7', 'VII'), ('8', 'VII')], max_length=3),
        ),
    ]
