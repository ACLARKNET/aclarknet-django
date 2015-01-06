# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aclarknet', '0003_auto_20150106_2052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='teammember',
            name='desc',
        ),
    ]
