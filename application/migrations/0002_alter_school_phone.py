# Generated by Django 3.2.3 on 2021-05-29 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='phone',
            field=models.CharField(max_length=20),
        ),
    ]