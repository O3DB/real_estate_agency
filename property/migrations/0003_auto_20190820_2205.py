# Generated by Django 2.2.4 on 2019-08-20 19:05

from django.db import migrations


def set_new_buildings(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Flat.objects.filter(construction_year__gte=2015).update(new_building=True)
    Flat.objects.filter(construction_year__lt=2015)\
                .exclude(construction_year__isnull=True)\
                .update(new_building=False)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0002_flat_new_building'),
    ]

    operations = [
        migrations.RunPython(set_new_buildings)
    ]
