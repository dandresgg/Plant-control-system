# Generated by Django 3.0.3 on 2020-02-12 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registry',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='registers/picture'),
        ),
    ]
