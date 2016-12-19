# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('birth_reminder', '0003_auto_20161218_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='message_id',
            field=models.ForeignKey(to='birth_reminder.Messages'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='send_time',
            field=models.TimeField(),
        ),
    ]
