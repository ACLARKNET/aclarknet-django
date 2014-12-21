# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aclarknet', '0008_service_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammember',
            name='desc',
            field=models.CharField(default=None, max_length=60),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='teammember',
            name='icon',
            field=models.CharField(default=None, max_length=30),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='teammember',
            name='text',
            field=models.TextField(default=None),
            preserve_default=True,
        ),
    ]
