# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-09-12 14:49
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
                ('createTime', models.DateTimeField(auto_created=True)),
                ('gname', models.CharField(db_column='gname', max_length=20)),
                ('gdate', models.DateTimeField(db_column='gdate', null=True)),
                ('ggirlnum', models.IntegerField()),
                ('gboynum', models.IntegerField()),
                ('isDelete', models.BooleanField(default=False)),
                ('lastTime', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'grades',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createTime', models.DateTimeField(auto_created=True)),
                ('sname', models.CharField(max_length=20)),
                ('sgender', models.BooleanField()),
                ('sage', models.IntegerField()),
                ('scontent', models.CharField(max_length=20, null=True)),
                ('isDelete', models.BooleanField(default=False)),
                ('lastTime', models.DateTimeField(auto_now=True)),
                ('sGrades', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myFristApp.Grades')),
            ],
            options={
                'db_table': 'students',
                'ordering': ['id'],
            },
        ),
    ]
