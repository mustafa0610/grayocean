# Generated by Django 2.1.5 on 2019-03-17 03:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0006_blog_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='dislikes',
            field=models.ManyToManyField(blank=True, related_name='_comment_dislikes_+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='_comment_likes_+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.TextField(blank=True),
        ),
    ]