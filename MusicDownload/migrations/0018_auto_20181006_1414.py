# Generated by Django 2.1.1 on 2018-10-06 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MusicDownload', '0017_auto_20181005_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracks',
            name='track_language',
            field=models.CharField(max_length=50),
        ),
    ]