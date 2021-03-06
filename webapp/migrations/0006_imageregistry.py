# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-03-27 07:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_auto_20180324_1741'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageRegistry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.GenericIPAddressField(unique=True, verbose_name='IP\u5730\u5740')),
                ('label', models.CharField(max_length=32, verbose_name='\u5907\u6ce8')),
                ('type', models.CharField(max_length=30, verbose_name='API\u7c7b\u578b')),
                ('count', models.IntegerField(verbose_name='\u955c\u50cf\u6570\u91cf')),
                ('status', models.CharField(default='up', max_length=10, verbose_name='\u72b6\u6001')),
                ('createtime', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
            ],
        ),
    ]
