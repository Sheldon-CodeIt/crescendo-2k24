import uuid
from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields such as company description, location, etc.

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    description = models.TextField()
    date_of_release = models.DateField(auto_now_add=True)
    ingredients = models.ManyToManyField('Ingredient')
    additives = models.ManyToManyField('Additive')
    food_colorings = models.ManyToManyField('FoodColoring')
    minimum_age_for_consumption = models.IntegerField()
    recommended_age_for_consumption = models.IntegerField()
    recommended_intake = models.CharField(max_length=100)
    
    # Additional fields
    energy = models.FloatField(default=0.0)
    fibers = models.FloatField(default=0.0)
    fruit_percentage = models.FloatField(default=0.0)
    proteins = models.FloatField(default=0.0)
    saturated_fats = models.FloatField(default=0.0)
    sodium = models.FloatField(default=0.0)
    sugar = models.FloatField(default=0.0)
    product_type = models.CharField(max_length=10, choices=(('solid', 'Solid'), ('beverage', 'Beverage')))

    def __str__(self):
        return self.title




class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.name

class Additive(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    # Add other fields as needed

    def __str__(self):
        return self.name

class FoodColoring(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    # Add other fields as needed    

    def __str__(self):
        return self.name





