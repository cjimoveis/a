# Generated by Django 5.0.1 on 2024-02-17 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_listing_photo_10_listing_photo_11_listing_photo_12_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='video_1',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='video_2',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='video_3',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='video_4',
        ),
        migrations.AddField(
            model_name='listing',
            name='photo_16',
            field=models.ImageField(blank=True, upload_to='photos'),
        ),
        migrations.AddField(
            model_name='listing',
            name='photo_17',
            field=models.ImageField(blank=True, upload_to='photos'),
        ),
        migrations.AddField(
            model_name='listing',
            name='photo_18',
            field=models.ImageField(blank=True, upload_to='photos'),
        ),
    ]