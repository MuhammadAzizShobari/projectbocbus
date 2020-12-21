# Generated by Django 2.2 on 2020-12-11 05:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pengguna', '0004_databus_po_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='databus',
            name='harga',
            field=models.IntegerField(default=100000),
        ),
        migrations.AlterField(
            model_name='databus',
            name='kategori',
            field=models.CharField(choices=[('kecil', 'Kecil'), ('medium', 'Medium'), ('besar', 'Besar')], default=None, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='databus',
            name='po_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='po_id', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='databus',
            name='tahun_pembuatan',
            field=models.IntegerField(default=2015),
        ),
        migrations.AlterField(
            model_name='databus',
            name='tambahan',
            field=models.TextField(default=None, null=True),
        ),
    ]