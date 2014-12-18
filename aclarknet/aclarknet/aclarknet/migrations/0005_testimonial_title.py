# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aclarknet', '0004_testimonial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='title',
            field=models.CharField(default=None, max_length=90),
            preserve_default=True,
        ),
    ]
