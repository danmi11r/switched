# Generated by Django 4.2.6 on 2023-12-04 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('switched_app', '0006_remove_game_img_src_game_cover_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='game_url',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]