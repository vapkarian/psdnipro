# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-09 14:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teammember',
            name='category',
        ),
        migrations.AddField(
            model_name='teammember',
            name='categories',
            field=models.ManyToManyField(related_name='members', to='news.Category', verbose_name='Категорії'),
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='news.Category', verbose_name='Категорія'),
        ),
        migrations.AlterField(
            model_name='document',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='news.Category', verbose_name='Категорія'),
        ),
    ]
