# Generated by Django 3.0.5 on 2020-04-29 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0009_auto_20200429_0837'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customcaroption',
            name='model_version_line_package',
        ),
        migrations.RemoveField(
            model_name='packagecustomcar',
            name='model_version_line_package',
        ),
        migrations.AddField(
            model_name='customcaroption',
            name='package',
            field=models.ManyToManyField(through='car.PackageCustomCar', to='car.Package'),
        ),
        migrations.AddField(
            model_name='packagecustomcar',
            name='package',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='car.Package'),
        ),
    ]