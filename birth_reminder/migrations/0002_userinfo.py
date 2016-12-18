# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('birth_reminder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('doctor_id', models.IntegerField(serialize=False, primary_key=True)),
                ('username', models.CharField(max_length=200)),
                ('send_time', models.TimeField()),
                ('message_id', models.ForeignKey(to='birth_reminder.Messages')),
            ],
        ),
    ]
