# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-01-26 22:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200124_0529'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='products'),
        ),
    ]
