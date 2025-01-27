# Generated by Django 5.0.7 on 2024-07-27 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_app', '0002_movies_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='images',
            field=models.ImageField(default=1, upload_to='media/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movies',
            name='video',
            field=models.FileField(upload_to='videos/'),
        ),
    ]
