# Generated by Django 5.0.6 on 2024-07-01 04:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0004_passengers'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Passengers',
            new_name='Passenger',
        ),
    ]