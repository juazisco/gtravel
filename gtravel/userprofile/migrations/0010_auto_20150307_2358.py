# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0009_remove_persona_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='facebook',
            field=models.URLField(verbose_name='Facebook Profile', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='persona',
            name='googleplus',
            field=models.URLField(verbose_name='Google+ Profile', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='persona',
            name='phone_number',
            field=models.CharField(max_length=15, verbose_name='Phone number', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='persona',
            name='twitter',
            field=models.URLField(verbose_name='Twitter Profile', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='persona',
            name='website',
            field=models.URLField(verbose_name='Website or blog', null=True),
            preserve_default=True,
        ),
    ]
