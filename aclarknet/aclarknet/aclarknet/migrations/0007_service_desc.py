# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aclarknet', '0006_service_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='desc',
            field=models.CharField(default=None, max_length=60),
            preserve_default=False,
        ),
    ]
