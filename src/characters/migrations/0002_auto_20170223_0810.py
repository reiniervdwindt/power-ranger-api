# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-02-23 08:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='villain',
            name='type',
            field=models.CharField(blank=True, choices=[(b'boss', b'Boss'), (b'minion', b'Minion')], default=None, max_length=32, null=True),
        ),
    ]
