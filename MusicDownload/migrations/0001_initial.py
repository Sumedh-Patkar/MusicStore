# Generated by Django 2.1.1 on 2018-10-02 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tracks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('track_name', models.CharField(max_length=100)),
                ('track_length', models.IntegerField()),
                ('track_image', models.ImageField(upload_to='')),
                ('track_album', models.CharField(max_length=100)),
                ('track_artist', models.CharField(max_length=100)),
            ],
        ),
    ]
