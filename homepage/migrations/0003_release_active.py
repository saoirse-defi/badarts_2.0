# Generated by Django 4.0 on 2021-12-23 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='release',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
