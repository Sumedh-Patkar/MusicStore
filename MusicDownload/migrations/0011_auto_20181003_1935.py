# Generated by Django 2.1.1 on 2018-10-03 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MusicDownload', '0010_auto_20181003_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracks',
            name='track_image',
            field=models.ImageField(upload_to=''),
        ),
    ]
