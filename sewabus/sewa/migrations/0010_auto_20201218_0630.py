# Generated by Django 2.2 on 2020-12-18 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sewa', '0009_auto_20201218_0630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sewa',
            name='no_hp',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sewa',
            name='no_ktp',
            field=models.IntegerField(null=True),
        ),
    ]