# Generated by Django 4.0 on 2022-04-09 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0003_video_artist'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='youtube_id',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='data_caption',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='description',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
