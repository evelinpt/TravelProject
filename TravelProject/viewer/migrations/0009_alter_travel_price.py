# Generated by Django 4.0.3 on 2022-04-09 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0008_alter_travel_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travel',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
