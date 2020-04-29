# Generated by Django 3.0.5 on 2020-04-29 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0008_auto_20200427_1204'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactChannel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.BooleanField()),
                ('call', models.BooleanField()),
                ('sns', models.BooleanField()),
                ('sms', models.BooleanField()),
                ('fax', models.BooleanField()),
                ('email', models.BooleanField()),
            ],
            options={
                'db_table': 'custom_channels',
            },
        ),
        migrations.RemoveField(
            model_name='customcaroption',
            name='package',
        ),
        migrations.RemoveField(
            model_name='modelversionlinepackage',
            name='custom_car_option',
        ),
        migrations.AddField(
            model_name='customcar',
            name='privacy_check',
            field=models.BooleanField(default=None),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='PackageCustomCar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('custom_car_option', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='car.CustomCarOption')),
                ('model_version_line_package', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='car.ModelVersionLinePackage')),
            ],
            options={
                'db_table': 'package_custom_cars',
            },
        ),
        migrations.AddField(
            model_name='customcar',
            name='contact_channel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='car.ContactChannel'),
        ),
        migrations.AddField(
            model_name='customcaroption',
            name='model_version_line_package',
            field=models.ManyToManyField(through='car.PackageCustomCar', to='car.ModelVersionLinePackage'),
        ),
    ]