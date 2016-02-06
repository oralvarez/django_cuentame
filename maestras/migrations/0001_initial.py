# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-06 03:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('iso', models.CharField(max_length=4)),
            ],
            options={
                'verbose_name_plural': 'Countries',
            },
        ),
    ]
