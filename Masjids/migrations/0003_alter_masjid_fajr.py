# Generated by Django 3.2.2 on 2021-05-12 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Masjids', '0002_alter_masjid_fajr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='masjid',
            name='fajr',
            field=models.CharField(max_length=100),
        ),
    ]
