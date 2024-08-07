# Generated by Django 5.0.6 on 2024-07-13 03:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_myuser_first_name_myuser_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.JSONField(blank=True),
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]
