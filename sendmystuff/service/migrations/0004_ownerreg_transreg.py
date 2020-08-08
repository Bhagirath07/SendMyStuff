# Generated by Django 3.0.7 on 2020-08-07 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_auto_20200807_1448'),
    ]

    operations = [
        migrations.CreateModel(
            name='OwnerReg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50)),
                ('contact', models.CharField(max_length=20)),
                ('dob', models.DateField()),
                ('password', models.CharField(max_length=10)),
                ('cpassword', models.CharField(max_length=10)),
                ('company', models.CharField(max_length=30)),
                ('uidaino', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TransReg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50)),
                ('contact', models.CharField(max_length=20)),
                ('dob', models.DateField()),
                ('password', models.CharField(max_length=10)),
                ('cpassword', models.CharField(max_length=10)),
                ('company', models.CharField(max_length=30)),
                ('nouidai', models.IntegerField()),
                ('nogst', models.IntegerField()),
                ('nopan', models.IntegerField()),
            ],
        ),
    ]
