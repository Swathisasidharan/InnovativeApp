# Generated by Django 2.1.1 on 2018-11-19 14:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Task_Id', models.CharField(max_length=10, unique=True, verbose_name='Task ID')),
                ('Task_desc', models.CharField(max_length=200, verbose_name='Task Description')),
                ('Task_date_time', models.DateField(default=datetime.date.today, verbose_name='Current Date')),
                ('Task_status', models.CharField(choices=[('progress', 'In Progress'), ('completed', 'Completed'), ('pending', 'Pending')], default='progress', max_length=2)),
                ('Task_created', models.DateField(default=datetime.date.today, verbose_name='Created Date')),
                ('Task_modified', models.DateField(default=datetime.date.today, verbose_name='Modified Date')),
            ],
        ),
        migrations.CreateModel(
            name='to_proxy',
            fields=[
            ],
            options={
                'verbose_name': 'Task Id',
                'verbose_name_plural': 'Task ids',
                'proxy': True,
                'indexes': [],
            },
            bases=('to_do_app.task_details',),
        ),
    ]
