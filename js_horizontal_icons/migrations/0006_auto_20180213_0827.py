# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('js_horizontal_icons', '0005_auto_20180213_0825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horizontaliconmodel',
            name='icon',
            field=models.CharField(null=True, help_text='Use FA name without prepended "fa-", example: "address-book".  Find <a href="https://fontawesome.com/icons" href="_blank">FontAwesome Icons</a>', blank=True, max_length=255),
        ),
    ]
