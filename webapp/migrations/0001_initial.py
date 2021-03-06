# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-03-21 15:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='platformcluster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='\u96c6\u7fa4\u540d')),
                ('version', models.CharField(max_length=32, verbose_name='\u7248\u672c')),
                ('createtime', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
            ],
        ),
        migrations.CreateModel(
            name='platformcomponent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='\u5bb9\u5668\u540d')),
                ('type', models.CharField(max_length=20, verbose_name='\u7ec4\u4ef6\u7c7b\u578b')),
                ('netmode', models.CharField(max_length=32, verbose_name='\u7f51\u7edc\u6a21\u5f0f')),
                ('image', models.CharField(max_length=255, verbose_name='\u955c\u50cf\u540d')),
                ('cport', models.CharField(max_length=10, verbose_name='\u5bb9\u5668\u7aef\u53e3')),
                ('hport', models.CharField(max_length=10, verbose_name='\u4e3b\u673a\u7aef\u53e3')),
                ('env', models.CharField(blank=True, max_length=512, null=True, verbose_name='\u73af\u5883\u53d8\u91cf')),
                ('volume', models.CharField(blank=True, max_length=512, null=True, verbose_name='\u5377\u6620\u5c04')),
                ('createtime', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('cluster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.platformcluster', verbose_name='\u96c6\u7fa4')),
            ],
        ),
        migrations.CreateModel(
            name='platformhosts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(blank=True, max_length=32, null=True, verbose_name='\u4e3b\u673a\u540d')),
                ('address', models.CharField(max_length=32, verbose_name='IP\u5730\u5740')),
                ('sversion', models.CharField(blank=True, max_length=32, null=True, verbose_name='\u7cfb\u7edf\u7248\u672c')),
                ('dversion', models.CharField(blank=True, max_length=32, null=True, verbose_name='docker\u7248\u672c')),
                ('ddriver', models.CharField(blank=True, max_length=32, null=True, verbose_name='docker\u5b58\u50a8\u9a71\u52a8')),
                ('ddata', models.CharField(blank=True, max_length=32, null=True, verbose_name='docker\u5b58\u50a8\u76ee\u5f55')),
                ('cpu', models.CharField(blank=True, max_length=32, null=True, verbose_name='CPU')),
                ('mem', models.CharField(blank=True, max_length=32, null=True, verbose_name='\u5185\u5b58')),
                ('status', models.CharField(default='down', max_length=10, verbose_name='CPU')),
            ],
        ),
        migrations.CreateModel(
            name='platformtemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='\u6a21\u7248\u540d')),
                ('label', models.CharField(max_length=64, verbose_name='\u8bf4\u660e')),
                ('type', models.CharField(max_length=20, verbose_name='\u6a21\u7248\u7c7b\u578b')),
                ('image', models.CharField(max_length=255, verbose_name='\u955c\u50cf\u540d')),
                ('netmode', models.CharField(max_length=32, verbose_name='\u7f51\u7edc\u6a21\u5f0f')),
                ('cport', models.CharField(max_length=10, verbose_name='\u5bb9\u5668\u7aef\u53e3')),
                ('hport', models.CharField(max_length=10, verbose_name='\u4e3b\u673a\u7aef\u53e3')),
                ('env', models.TextField(blank=True, null=True, verbose_name='\u73af\u5883\u53d8\u91cf')),
                ('volume', models.TextField(blank=True, max_length=512, null=True, verbose_name='\u5377\u6620\u5c04')),
                ('dockerfile', models.TextField(blank=True, null=True)),
                ('createtime', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
            ],
        ),
        migrations.AddField(
            model_name='platformcomponent',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.platformhosts', verbose_name='\u4e3b\u673aIP'),
        ),
        migrations.AddField(
            model_name='platformcomponent',
            name='template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.platformtemplate', verbose_name='\u4f7f\u7528\u6a21\u7248'),
        ),
    ]
