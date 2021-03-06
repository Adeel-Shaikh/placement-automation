# Generated by Django 3.1.7 on 2021-04-10 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20210410_0903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentresume',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('Other', 'Prefer Not to Say')], max_length=20),
        ),
        migrations.AlterField(
            model_name='studentresume',
            name='hsc',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='studentresume',
            name='sem1',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='studentresume',
            name='sem2',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='studentresume',
            name='sem3',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='studentresume',
            name='sem4',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='studentresume',
            name='sem5',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='studentresume',
            name='sem6',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='studentresume',
            name='sem7',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='studentresume',
            name='sem8',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='studentresume',
            name='ssc',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
    ]
