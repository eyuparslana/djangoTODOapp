# Generated by Django 2.2.1 on 2019-05-08 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TODOapp', '0004_auto_20190508_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
