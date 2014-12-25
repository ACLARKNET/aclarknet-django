# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aclarknet', '0015_auto_20141225_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='icon',
            field=models.CharField(default=None, max_length=30, null=True),
            preserve_default=True,
        ),
    ]
