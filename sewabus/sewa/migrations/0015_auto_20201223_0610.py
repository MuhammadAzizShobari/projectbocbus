# Generated by Django 2.2.12 on 2020-12-23 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sewa', '0014_auto_20201223_0610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sewa',
            name='nama_pemesan',
            field=models.CharField(blank=True, max_length=240),
        ),
    ]
