# Generated by Django 4.0.4 on 2022-05-25 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotelApp', '0010_rename_contact_contacting'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='bookings',
            new_name='booked',
        ),
    ]
