# Generated by Django 3.1.7 on 2022-11-20 09:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0011_auto_20221119_0148'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applylist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education', models.CharField(default='', max_length=200)),
                ('minsalary', models.CharField(default='', max_length=20)),
                ('maxsalary', models.CharField(default='', max_length=20)),
                ('resume', models.FileField(upload_to='resume')),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Account.jobdetails')),
            ],
        ),
    ]
