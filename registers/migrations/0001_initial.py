# Generated by Django 3.0.3 on 2020-02-11 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plant_name', models.CharField(max_length=20)),
                ('week_control', models.DateTimeField(blank=True)),
                ('water_consuption', models.FloatField(default=0)),
                ('active_nutrients', models.FloatField(default=0)),
                ('noactive_nutrients', models.FloatField(default=0)),
                ('size_control', models.FloatField(default=0)),
                ('picture', models.ImageField(blank=True, height_field=200, null=True, upload_to='registers/picture', width_field=200)),
                ('created', models.DateTimeField(auto_now=True)),
                ('modified', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
