# Generated by Django 2.0.8 on 2019-01-26 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_album_model_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='model_pic',
            field=models.ImageField(null=True, upload_to='static/pics'),
        ),
    ]
