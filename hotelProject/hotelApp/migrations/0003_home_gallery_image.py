# Generated by Django 4.0.4 on 2022-05-24 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelApp', '0002_home_bedroom2_image_home_bedroom3_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='gallery_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
