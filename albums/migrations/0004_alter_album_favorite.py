# Generated by Django 3.2.5 on 2021-07-31 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0003_album_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='favorite',
            field=models.BooleanField(default=False),
        ),
    ]
