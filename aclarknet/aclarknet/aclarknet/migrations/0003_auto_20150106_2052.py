# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aclarknet', '0002_auto_20150106_1547'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testimonial',
            name='title',
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='name',
            field=models.CharField(max_length=120),
            preserve_default=True,
        ),
    ]
