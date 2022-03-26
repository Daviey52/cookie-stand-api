# Generated by Django 4.0.3 on 2022-03-26 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('things', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='thing',
            old_name='name',
            new_name='location',
        ),
        migrations.AddField(
            model_name='thing',
            name='average_cookies_per_sale',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='thing',
            name='hourly_sales',
            field=models.JSONField(default=list, null=True),
        ),
        migrations.AddField(
            model_name='thing',
            name='maximum_customers_per_hour',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='thing',
            name='minimum_customers_per_hour',
            field=models.IntegerField(default=0),
        ),
    ]