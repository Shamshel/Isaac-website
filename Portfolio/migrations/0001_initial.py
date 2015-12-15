# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import Portfolio.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('abstract', models.CharField(max_length=200, null=True, blank=True)),
                ('text', models.TextField()),
                ('link', models.CharField(max_length=200, null=True, blank=True)),
                ('image', models.ImageField(null=True, upload_to=Portfolio.models.get_image_path, blank=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published', models.BooleanField(default=False)),
                ('published_date', models.DateTimeField(null=True, blank=True)),
                ('modified_date', models.DateTimeField(null=True, blank=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
