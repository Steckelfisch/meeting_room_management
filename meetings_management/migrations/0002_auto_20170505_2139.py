# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-05 21:39
from __future__ import unicode_literals

import datetime
from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('meetings_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeetingRoomUser',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('metadata', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={}, verbose_name='metadata')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date and time of creation')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='date and time of last update')),
                ('role', models.PositiveSmallIntegerField(choices=[(0, 'Employee'), (1, 'Administrator')], default=0, verbose_name='Role')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='meeting_room_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'meeting room user',
                'verbose_name_plural': 'meeting room users',
            },
        ),
        migrations.AlterField(
            model_name='meetingroom',
            name='available_from',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 5, 6, 0, 0, 222236, tzinfo=utc), verbose_name='available from'),
        ),
        migrations.AlterField(
            model_name='meetingroom',
            name='available_until',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 5, 21, 0, 0, 222296, tzinfo=utc), verbose_name='available until'),
        ),
    ]
