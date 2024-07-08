from django.db import models

# Create your models here.
class Author(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.first} {self.last}"

class Recipe(models.Model):
    REGIONS = {
        "RegionI" : "Ilocos Region",
        "RegionII" : "Cagayan Valley",
        "RegionIII" : "Central Luzon",
        "RegionIV‑A" : "CALABARZON",
        "MIMAROPA" : "MIMAROPA Region",
        "RegionV" : "Bicol Region",
        "CAR" : "Cordillera Administrative Region",
        "NCR" : "National Capital Region" 
    }

    name = models.CharField(max_length=171)
    description = models.CharField(max_length=750)
    region = models.CharField(max_length=10, choices=REGIONS)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="recipes")
    ingredients = models.JSONField()

    def __str__(self):
        return f"{self.name}, desc: {self.description}, region: {self.region}, author: {self.author}, ingredients: {self.ingredients}"