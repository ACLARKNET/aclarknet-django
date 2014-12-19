# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aclarknet', '0005_testimonial_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='text',
            field=models.TextField(default=None),
            preserve_default=True,
        ),
    ]
