# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='screen',
            name='caption',
            field=models.CharField(default='', max_length=255, blank=True),
            preserve_default=True,
        ),
    ]
