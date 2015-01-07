# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aclarknet', '0004_auto_20150106_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='icon',
            field=models.ImageField(upload_to=b''),
            preserve_default=True,
        ),
    ]
