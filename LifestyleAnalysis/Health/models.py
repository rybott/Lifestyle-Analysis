from django.db import models

# Ingredients Table
class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    portion_grams = models.FloatField()
    ounces = models.FloatField()
    calories = models.FloatField()
    sugar_grams = models.FloatField()
    sat_fat_grams = models.FloatField()
    protein_grams = models.FloatField()
    fiber_grams = models.FloatField()
    purchase_location = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)

# Premade Meals Table
class PremadeMeal(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    portion_grams = models.FloatField()
    ounces = models.FloatField()
    calories = models.FloatField()
    sugar_grams = models.FloatField()
    sat_fat_grams = models.FloatField()
    protein_grams = models.FloatField()
    fiber_grams = models.FloatField()
    purchase_location = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)

# Homemade Meals Table
class HomemadeMeal(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    portion_grams = models.FloatField()
    ounces = models.FloatField()
    calories = models.FloatField()
    sugar_grams = models.FloatField()
    sat_fat_grams = models.FloatField()
    protein_grams = models.FloatField()
    fiber_grams = models.FloatField()
    purchase_location = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)

# Recipes Table
class Recipe(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    total_portion_grams = models.FloatField()
    serving_grams = models.FloatField()
    serving_ounces = models.FloatField()
    serving_calories = models.FloatField()
    serving_sugar_grams = models.FloatField()
    serving_fat_grams = models.FloatField()
    serving_protein_grams = models.FloatField()
    serving_fiber_grams = models.FloatField()
    purchase_location = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)

# RecipeIngredients Table
class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField()

# KcalIn Table
class KcalIn(models.Model):
    date = models.DateField()
    ingredient = models.ForeignKey(Ingredient, on_delete=models.SET_NULL, null=True, blank=True)
    premade_meal = models.ForeignKey(PremadeMeal, on_delete=models.SET_NULL, null=True, blank=True)
    homemade_meal = models.ForeignKey(HomemadeMeal, on_delete=models.SET_NULL, null=True, blank=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.SET_NULL, null=True, blank=True)
    quantity_grams = models.FloatField()
