# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('birth_reminder', '0005_auto_20161218_1255'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctormessagemapping',
            old_name='doctot',
            new_name='user',
        ),
    ]
