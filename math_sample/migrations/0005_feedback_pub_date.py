# Generated by Django 2.1.7 on 2020-04-08 08:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('math_sample', '0004_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
