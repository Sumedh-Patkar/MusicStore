# Generated by Django 2.1.1 on 2018-10-03 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MusicDownload', '0009_remove_tracks_actual_track'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracks',
            name='track_image',
            field=models.FileField(upload_to=''),
        ),
    ]