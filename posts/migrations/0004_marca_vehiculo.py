# Generated by Django 3.1.2 on 2020-10-21 13:29

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20201021_0748'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('descripcion', models.CharField(max_length=200)),
                ('creacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('actualizacion', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=10, unique=True)),
                ('referencia', models.CharField(max_length=20)),
                ('nota', models.TextField()),
                ('estaeliminado', models.BooleanField(default=False)),
                ('creacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('actualizacion', models.DateTimeField(blank=True, null=True)),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='posts.marca')),
            ],
        ),
    ]
