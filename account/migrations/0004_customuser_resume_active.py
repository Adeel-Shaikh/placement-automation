# Generated by Django 3.1.7 on 2021-04-10 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20210406_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='resume_active',
            field=models.BooleanField(default=False),
        ),
    ]
