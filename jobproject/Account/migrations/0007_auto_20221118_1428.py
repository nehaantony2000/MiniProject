# Generated by Django 3.1.7 on 2022-11-18 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0006_auto_20221118_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobdetails',
            name='jobdescription',
            field=models.TextField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='jobdetails',
            name='qualification',
            field=models.TextField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='jobdetails',
            name='responsibility',
            field=models.TextField(default='', max_length=500),
        ),
    ]
