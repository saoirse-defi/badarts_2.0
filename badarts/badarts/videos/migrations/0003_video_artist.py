# Generated by Django 4.0 on 2022-04-07 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_artist_bio_alter_release_artist'),
        ('videos', '0002_video_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='artist',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='homepage.artist'),
        ),
    ]
