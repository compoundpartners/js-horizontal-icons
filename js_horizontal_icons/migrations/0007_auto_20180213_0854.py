# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('js_horizontal_icons', '0006_auto_20180213_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horizontaliconmodel',
            name='icon',
            field=models.CharField(help_text='Use full fa string, for example: "fab fa-bitcoin".  Find <a href="https://fontawesome.com/icons" href="_blank">FontAwesome Icons</a>', max_length=255, null=True, blank=True),
        ),
    ]
