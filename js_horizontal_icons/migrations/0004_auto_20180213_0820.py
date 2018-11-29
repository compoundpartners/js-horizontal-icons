# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('js_horizontal_icons', '0003_auto_20180209_0729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horizontaliconmodel',
            name='icon',
            field=models.CharField(max_length=255, blank=True, null=True),
        ),
    ]
