# Generated by Django 3.0.7 on 2020-08-07 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_ownerreg_transreg'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transreg',
            old_name='cpassword',
            new_name='conpass',
        ),
    ]
