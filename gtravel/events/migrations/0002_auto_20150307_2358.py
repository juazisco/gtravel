# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_type',
            field=models.IntegerField(max_length=1, choices=[('Small Event', ((0, 'Hackfest'), (1, 'Other'))), ('Large Event', ((2, 'GUADEC'), (3, 'GNOME.ASIA'), (4, 'Other')))]),
            preserve_default=True,
        ),
    ]
