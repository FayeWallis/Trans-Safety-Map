# Generated by Django 4.1 on 2022-08-09 01:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0003_incident_delete_incidents'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='incident',
            options={'managed': False, 'verbose_name_plural': 'Incidents'},
        ),
    ]