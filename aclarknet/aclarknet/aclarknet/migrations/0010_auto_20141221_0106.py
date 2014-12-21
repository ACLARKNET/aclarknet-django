# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aclarknet', '0009_auto_20141220_1552'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='client_name',
        ),
        migrations.AddField(
            model_name='client',
            name='name',
            field=models.CharField(default=None, max_length=60),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='client',
            name='text',
            field=models.TextField(default=None),
            preserve_default=True,
        ),
    ]
