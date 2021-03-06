# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('customerid', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=120, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.IntegerField()),
            ],
        ),
    ]
