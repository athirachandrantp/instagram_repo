# Generated by Django 4.2.5 on 2023-10-04 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instaapp', '0008_rename_post_videofile_posts_post_video_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='post_video',
            field=models.FileField(null=True, upload_to='images/%Y', verbose_name=''),
        ),
    ]
