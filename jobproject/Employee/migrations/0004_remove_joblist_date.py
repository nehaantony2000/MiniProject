# Generated by Django 3.1.7 on 2022-10-27 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0003_joblist_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='joblist',
            name='date',
        ),
    ]