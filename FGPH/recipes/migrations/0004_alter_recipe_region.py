# Generated by Django 5.0.6 on 2024-07-13 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_alter_recipe_author_alter_recipe_ingredients_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='region',
            field=models.CharField(choices=[('RegionI', 'Ilocos Region'), ('RegionII', 'Cagayan Valley'), ('RegionIII', 'Central Luzon'), ('RegionIV‑A', 'CALABARZON'), ('MIMAROPA', 'MIMAROPA Region'), ('RegionV', 'Bicol Region'), ('CAR', 'Cordillera Administrative Region'), ('NCR', 'National Capital Region')], max_length=64),
        ),
    ]
