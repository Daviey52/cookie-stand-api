# Generated by Django 4.0.3 on 2022-03-26 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('things', '0002_rename_name_thing_location_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='thing',
            old_name='location',
            new_name='name',
        ),
    ]