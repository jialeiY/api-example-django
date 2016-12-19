# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('birth_reminder', '0004_auto_20161218_1251'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctormessagemapping',
            old_name='doctor_id',
            new_name='doctot',
        ),
        migrations.RenameField(
            model_name='doctormessagemapping',
            old_name='message_id',
            new_name='message',
        ),
        migrations.RenameField(
            model_name='userinfo',
            old_name='message_id',
            new_name='message',
        ),
    ]
