# Generated by Django 3.1.2 on 2020-10-29 22:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testbills', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bill',
            name='items',
        ),
        migrations.AddField(
            model_name='item',
            name='bill',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='testbills.bill'),
            preserve_default=False,
        ),
    ]
