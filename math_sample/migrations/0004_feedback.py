# Generated by Django 2.1.7 on 2020-03-31 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('math_sample', '0003_auto_20190402_1548'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
                ('text', models.TextField()),
            ],
        ),
    ]
