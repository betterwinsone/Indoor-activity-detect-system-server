# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-22 15:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='hongwai',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idnum', models.IntegerField()),
                ('time', models.CharField(max_length=30)),
                ('distance', models.FloatField()),
            ],
        ),
    ]
