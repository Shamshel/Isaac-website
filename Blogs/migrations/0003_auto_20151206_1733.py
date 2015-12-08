# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import Blogs.models


class Migration(migrations.Migration):

    dependencies = [
        ('Blogs', '0002_post_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='abstract',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to=Blogs.models.get_image_path, blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='modified_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
