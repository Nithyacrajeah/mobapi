# Generated by Django 4.1 on 2022-08-24 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mobiles',
            name='rating',
            field=models.FloatField(default=3, null=True),
        ),
    ]
