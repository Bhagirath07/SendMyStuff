# Generated by Django 3.0.7 on 2020-08-08 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0008_auto_20200808_2058'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ownerreg',
            old_name='ucompany',
            new_name='company',
        ),
        migrations.RenameField(
            model_name='ownerreg',
            old_name='ucontact',
            new_name='contact',
        ),
        migrations.RenameField(
            model_name='ownerreg',
            old_name='ucpwd',
            new_name='cpwd',
        ),
        migrations.RenameField(
            model_name='ownerreg',
            old_name='udob',
            new_name='dob',
        ),
        migrations.RenameField(
            model_name='ownerreg',
            old_name='driverno',
            new_name='driver',
        ),
        migrations.RenameField(
            model_name='ownerreg',
            old_name='uemail',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='ownerreg',
            old_name='gstuser',
            new_name='gst',
        ),
        migrations.RenameField(
            model_name='ownerreg',
            old_name='uname',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='ownerreg',
            old_name='upwd',
            new_name='pwd',
        ),
        migrations.RenameField(
            model_name='ownerreg',
            old_name='routeopr',
            new_name='route',
        ),
        migrations.RenameField(
            model_name='ownerreg',
            old_name='truckno',
            new_name='truck',
        ),
        migrations.RemoveField(
            model_name='ownerreg',
            name='uidaiuser',
        ),
        migrations.AddField(
            model_name='ownerreg',
            name='uidai',
            field=models.IntegerField(default=''),
        ),
    ]