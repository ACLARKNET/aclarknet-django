# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('icon', models.CharField(default=None, max_length=30, null=True)),
                ('name', models.CharField(default=None, max_length=60)),
                ('text', models.TextField(default=None)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60)),
                ('desc', models.CharField(max_length=60)),
                ('icon', models.CharField(default=None, max_length=30)),
                ('text', models.TextField(default=None)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60)),
                ('desc', models.CharField(default=None, max_length=60)),
                ('icon', models.CharField(default=None, max_length=30)),
                ('text', models.TextField(default=None)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60)),
                ('title', models.CharField(default=None, max_length=120)),
                ('text', models.TextField()),
                ('date', models.DateTimeField(default=None)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
