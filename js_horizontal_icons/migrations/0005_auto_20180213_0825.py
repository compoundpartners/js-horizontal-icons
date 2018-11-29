# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('js_horizontal_icons', '0004_auto_20180213_0820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horizontaliconmodel',
            name='icon',
            field=models.CharField(null=True, blank=True, help_text='Use FA name without prepended "fa-", example: "address-book".  Find <a href="https://fontawesome.com/icons">FontAwesome Icons</a>', max_length=255),
        ),
    ]
