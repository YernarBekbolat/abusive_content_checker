# Generated by Django 5.0.6 on 2024-07-05 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0013_delete_retweet'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='is_abusive',
            field=models.BooleanField(default=False),
        ),
    ]
