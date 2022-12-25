# Generated by Django 3.1.7 on 2022-12-25 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CityWeatherCrud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=20)),
                ('temp', models.IntegerField()),
                ('pressure', models.IntegerField()),
                ('humidity', models.IntegerField()),
                ('visibility', models.IntegerField()),
                ('wind_speed', models.IntegerField()),
            ],
        ),
    ]