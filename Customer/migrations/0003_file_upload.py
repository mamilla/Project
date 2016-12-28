# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0002_transaction'),
    ]

    operations = [
        migrations.CreateModel(
            name='File_upload',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('files', models.FileField(upload_to=b'')),
                ('number', models.CharField(max_length=5)),
            ],
        ),
    ]
