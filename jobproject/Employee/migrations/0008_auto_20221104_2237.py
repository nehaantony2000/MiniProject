# Generated by Django 3.1.7 on 2022-11-04 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0007_auto_20221104_1806'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Joblist',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='is_employee',
        ),
    ]