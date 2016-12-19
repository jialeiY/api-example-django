# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message_name', models.CharField(max_length=200)),
                ('message_subject', models.CharField(max_length=1000)),
                ('message_text', models.TextField()),
            ],
        ),
    ]
