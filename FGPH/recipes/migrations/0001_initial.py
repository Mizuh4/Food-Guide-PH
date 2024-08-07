# Generated by Django 5.0.6 on 2024-07-10 08:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('username', models.CharField(max_length=64)),
                ('date_of_birth', models.DateField()),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=64)),
                ('last', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=171)),
                ('description', models.CharField(max_length=750)),
                ('region', models.CharField(choices=[('RegionI', 'Ilocos Region'), ('RegionII', 'Cagayan Valley'), ('RegionIII', 'Central Luzon'), ('RegionIV‑A', 'CALABARZON'), ('MIMAROPA', 'MIMAROPA Region'), ('RegionV', 'Bicol Region'), ('CAR', 'Cordillera Administrative Region'), ('NCR', 'National Capital Region')], max_length=10)),
                ('ingredients', models.JSONField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to='recipes.author')),
            ],
        ),
    ]
