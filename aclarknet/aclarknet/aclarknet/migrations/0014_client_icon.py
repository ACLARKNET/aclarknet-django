# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aclarknet', '0013_auto_20141221_2236'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='icon',
            field=models.CharField(default=None, max_length=30),
            preserve_default=True,
        ),
    ]
