# Generated by Django 4.2.5 on 2023-10-03 06:02

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_profile_profile_photo'),
        ('instaapp', '0004_rename_username_likepost_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentPost',
            fields=[
                ('body', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
                ('posts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instaapp.posts')),
            ],
        ),
    ]
