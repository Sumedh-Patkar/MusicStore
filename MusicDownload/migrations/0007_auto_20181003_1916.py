# Generated by Django 2.1.1 on 2018-10-03 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MusicDownload', '0006_auto_20181003_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracks',
            name='actual_track',
            field=models.FileField(blank=True, null=True, upload_to='.'),
        ),
    ]
