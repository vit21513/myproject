# Generated by Django 4.2.4 on 2023-09-01 14:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('semin2_app', '0008_alter_kicks_kick_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kicks',
            name='kick_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 1, 17, 40, 43, 257770)),
        ),
    ]
