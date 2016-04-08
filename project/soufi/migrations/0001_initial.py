# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('ts', models.DateTimeField(default=django.utils.timezone.now)),
                ('msg', models.TextField()),
                ('hashkey', models.CharField(max_length=6)),
            ],
        ),
    ]
