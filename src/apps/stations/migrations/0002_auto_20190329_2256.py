# Generated by Django 2.1.2 on 2019-03-29 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locationmodel',
            name='id',
            field=models.CharField(default='loc_20193292256260c8542c6', max_length=30, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='stationmodel',
            name='id',
            field=models.CharField(default='sta_2019329225626ff35560d', max_length=30, primary_key=True, serialize=False, unique=True),
        ),
    ]
