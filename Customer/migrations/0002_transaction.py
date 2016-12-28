# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('txnid', models.CharField(max_length=10, null=True)),
                ('amount', models.DecimalField(max_digits=6, decimal_places=2)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('customerid', models.ForeignKey(to='Customer.Customer')),
            ],
        ),
    ]
