# Generated by Django 3.0.7 on 2020-08-07 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_auto_20200807_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientreg',
            name='contact',
            field=models.CharField(max_length=20),
        ),
    ]
