from django.contrib import admin
from .models import Company, Product, Ingredient, Additive, FoodColoring

# Register your models here.

admin.site.register(Company)
admin.site.register(Ingredient)
admin.site.register(Additive)
admin.site.register(FoodColoring)
admin.site.register(Product)
