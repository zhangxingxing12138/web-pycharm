# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-24 02:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PicTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(upload_to='booktest/')),
            ],
        ),
        migrations.AlterField(
            model_name='bookinfo',
            name='btitle',
            field=models.CharField(db_column='title', max_length=20, verbose_name='标题'),
        ),
    ]
