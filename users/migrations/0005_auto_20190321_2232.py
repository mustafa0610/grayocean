# Generated by Django 2.1.5 on 2019-03-21 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='score',
            field=models.IntegerField(),
        ),
    ]
