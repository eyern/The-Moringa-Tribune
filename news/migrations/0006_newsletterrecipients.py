# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-14 19:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_article_article_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsLetterRecipients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]