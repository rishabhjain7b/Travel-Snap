# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locate', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zone',
            name='adresse',
        ),
        migrations.RemoveField(
            model_name='zone',
            name='beschreibung',
        ),
        migrations.RemoveField(
            model_name='zone',
            name='kn_nr',
        ),
        migrations.RemoveField(
            model_name='zone',
            name='kuerzel',
        ),
    ]
