# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('birth_reminder', '0006_auto_20161218_1338'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='is_active',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
