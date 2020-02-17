# Generated by Django 3.0.3 on 2020-02-12 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0001_initial'),
        ('registers', '0003_auto_20200212_1152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registry',
            name='active_nutrients',
        ),
        migrations.RemoveField(
            model_name='registry',
            name='noactive_nutrients',
        ),
        migrations.RemoveField(
            model_name='registry',
            name='plant_name',
        ),
        migrations.AddField(
            model_name='registry',
            name='plant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='plants.Plants'),
        ),
    ]