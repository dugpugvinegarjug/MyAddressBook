# Generated by Django 5.0.1 on 2024-01-25 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addressBook', '0003_alter_address_countryid_alter_address_stateid'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]