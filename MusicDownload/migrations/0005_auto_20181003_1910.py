# Generated by Django 2.1.1 on 2018-10-03 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MusicDownload', '0004_auto_20181003_0227'),
    ]

    operations = [
        migrations.AddField(
            model_name='tracks',
            name='actual_track',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='tracks',
            name='track_image',
            field=models.ImageField(upload_to=''),
        ),
    ]
