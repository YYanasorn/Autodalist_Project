# Generated by Django 5.0.3 on 2024-04-04 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_parameter_inlet_puressure_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parameter',
            old_name='inletPressure',
            new_name='inlet_puressure',
        ),
    ]