# Generated by Django 2.2.1 on 2019-05-08 21:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('TODOapp', '0002_auto_20190508_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='modified',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
