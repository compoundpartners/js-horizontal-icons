# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('js_horizontal_icons', '0002_auto_20180208_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='horizontaliconscontainermodel',
            name='button_link',
            field=models.CharField(max_length=255, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='horizontaliconscontainermodel',
            name='button_text',
            field=models.CharField(max_length=255, blank=True, null=True),
        ),
    ]
