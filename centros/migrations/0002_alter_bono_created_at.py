# Generated by Django 4.0.6 on 2022-07-11 08:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('centros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bono',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 11, 8, 21, 11, 314199, tzinfo=utc)),
        ),
    ]