# Generated by Django 2.2.1 on 2019-05-08 21:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TODOapp', '0005_auto_20190508_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
