# Generated by Django 4.0 on 2022-04-07 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0006_artist_instgram_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='bio',
            field=models.TextField(default='', max_length=2048),
        ),
    ]
