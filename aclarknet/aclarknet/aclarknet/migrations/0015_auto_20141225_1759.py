# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aclarknet', '0014_client_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='icon',
            field=models.CharField(default=b'building', max_length=30),
            preserve_default=True,
        ),
    ]
