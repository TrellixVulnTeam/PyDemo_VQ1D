# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-09-04 13:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gname', models.CharField(max_length=20)),
                ('gdate', models.DateTimeField()),
                ('ggirlnum', models.IntegerField()),
                ('gboynum', models.IntegerField()),
                ('isDelete', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=20)),
                ('sgender', models.BooleanField()),
                ('sage', models.IntegerField()),
                ('scontent', models.CharField(max_length=20)),
                ('isDelete', models.BooleanField(default=False)),
                ('sGrades', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myFristApp.Grades')),
            ],
        ),
    ]
