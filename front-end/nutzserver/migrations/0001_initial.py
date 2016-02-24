# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-24 04:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EMFProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('nickname', models.CharField(max_length=50)),
                ('current_address', models.CharField(max_length=250)),
                ('former_address', models.CharField(max_length=250)),
                ('sex', models.CharField(max_length=2)),
                ('race', models.CharField(max_length=50)),
                ('birthdate', models.DateField()),
                ('age', models.IntegerField()),
                ('height', models.CharField(max_length=50)),
                ('weight', models.IntegerField()),
                ('build', models.CharField(max_length=50)),
                ('hair', models.CharField(max_length=50)),
                ('eyes', models.CharField(max_length=50)),
                ('marks', models.CharField(max_length=50)),
                ('competency_status', models.CharField(max_length=50)),
                ('legal_guardian_name', models.CharField(max_length=50)),
                ('legal_guardian_phone', models.CharField(max_length=50)),
                ('legal_guardian_address', models.CharField(max_length=250)),
                ('family_address', models.CharField(max_length=250)),
                ('family_phone', models.CharField(max_length=50)),
                ('school_address', models.CharField(max_length=250)),
                ('school_phone', models.CharField(max_length=50)),
                ('work_address', models.CharField(max_length=250)),
                ('photo', models.CharField(max_length=50)),
                ('work_phone', models.CharField(max_length=50)),
                ('diagnosis', models.CharField(max_length=150)),
                ('allergies', models.CharField(max_length=50)),
                ('medication', models.CharField(max_length=50)),
                ('physician_name', models.CharField(max_length=50)),
                ('physician_address', models.CharField(max_length=250)),
                ('physician_phone', models.CharField(max_length=50)),
                ('language', models.CharField(max_length=50)),
                ('protect_ability', models.CharField(max_length=50)),
                ('behavior_characteristics', models.CharField(max_length=250)),
                ('response_to_search', models.CharField(max_length=50)),
                ('pattern_of_movement', models.CharField(max_length=50)),
                ('places_frequented', models.CharField(max_length=50)),
                ('relevant_limitations', models.CharField(max_length=50)),
                ('probable_dress', models.CharField(max_length=50)),
                ('last_seen', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('time', models.DateTimeField()),
                ('contact_person', models.CharField(max_length=50)),
                ('contact_phone', models.CharField(max_length=50)),
                ('fact_sheet_name', models.CharField(max_length=50)),
                ('record_location', models.CharField(max_length=50)),
                ('area', models.CharField(max_length=50)),
                ('last_updated', models.DateTimeField()),
            ],
        ),
    ]
