# Generated by Django 2.0.9 on 2018-10-10 11:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20181009_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 10, 11, 27, 26, 515766, tzinfo=utc)),
        ),
    ]
