# Generated by Django 2.2.12 on 2020-12-23 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sewa', '0012_auto_20201222_0516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sewa',
            name='no_ktp',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
