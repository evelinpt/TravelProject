# Generated by Django 4.0.3 on 2022-04-09 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0006_travel_description_travel_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travel',
            name='price',
            field=models.FloatField(default='0'),
        ),
    ]
