# Generated by Django 4.0.6 on 2022-07-11 08:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bono',
            fields=[
                ('codigo', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('centro', models.IntegerField()),
                ('nombre_centro', models.CharField(max_length=60)),
                ('agente', models.IntegerField()),
                ('nombre_agente', models.CharField(max_length=60)),
                ('codpost', models.CharField(max_length=5)),
                ('poblacion', models.CharField(max_length=60)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2022, 7, 11, 8, 5, 26, 102054, tzinfo=utc))),
            ],
        ),
    ]
