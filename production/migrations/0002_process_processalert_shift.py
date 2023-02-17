# Generated by Django 4.1.7 on 2023-02-17 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ref_id', models.CharField(max_length=100)),
                ('unique_id', models.CharField(max_length=100)),
                ('cycle_number', models.CharField(max_length=100)),
                ('process_name', models.CharField(max_length=100)),
                ('cam_name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('start_time', models.CharField(max_length=100)),
                ('end_time', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=100)),
                ('temperature', models.CharField(default='NA', max_length=100)),
                ('min_temp', models.CharField(default='NA', max_length=100)),
                ('max_temp', models.CharField(default='NA', max_length=100)),
                ('spectro', models.CharField(default='NA', max_length=100)),
                ('spectro_time', models.CharField(default='NA', max_length=30)),
                ('power', models.CharField(default='NA', max_length=30)),
                ('weight', models.CharField(default='NA', max_length=30)),
                ('batch_status', models.CharField(default=False, max_length=50)),
                ('cycle_flag', models.BooleanField(default=False)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='processalert',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('furnace_name', models.CharField(max_length=100)),
                ('shift', models.CharField(max_length=100)),
                ('started_at', models.CharField(max_length=100)),
                ('cycle_number', models.CharField(max_length=100)),
                ('process_name', models.CharField(max_length=100)),
                ('process_limit', models.CharField(max_length=100)),
                ('mailflag', models.CharField(default=False, max_length=100)),
                ('exceeded', models.CharField(max_length=100)),
                ('hour', models.CharField(max_length=100)),
                ('read', models.CharField(default=False, max_length=200)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('start_time', models.CharField(blank=True, max_length=150, null=True)),
                ('end_time', models.CharField(blank=True, max_length=150, null=True)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
