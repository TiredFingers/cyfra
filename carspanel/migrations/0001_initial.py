# Generated by Django 3.1.5 on 2021-01-30 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('load_capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OreStore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('current_volume', models.IntegerField()),
                ('sio2', models.IntegerField(default=0)),
                ('fe', models.IntegerField(default=0)),
                ('wkt_coords', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.TextField()),
                ('load_capacity', models.IntegerField()),
                ('current_load', models.IntegerField()),
                ('xcoord', models.IntegerField(default=0)),
                ('ycoord', models.IntegerField(default=0)),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='carspanel.carmodel')),
            ],
        ),
    ]