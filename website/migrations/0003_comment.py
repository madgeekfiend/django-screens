# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_screen_caption'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('comment', models.CharField(max_length=255)),
                ('screen', models.ForeignKey(to='website.Screen')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
