# Generated by Django 4.2.5 on 2023-10-04 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instaapp', '0011_remove_posts_post_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='post_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
