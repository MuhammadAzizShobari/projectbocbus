# Generated by Django 2.2 on 2020-12-18 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sewa', '0006_auto_20201218_0535'),
    ]

    operations = [
        migrations.AddField(
            model_name='sewa',
            name='no_ktp',
            field=models.IntegerField(null=True),
        ),
    ]