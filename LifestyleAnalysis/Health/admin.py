from django.contrib import admin
from .models import Ingredient,PremadeMeal,HomemadeMeal,Recipe,RecipeIngredient,KcalIn

# Register your models here.
admin.site.register(Ingredient)
admin.site.register(PremadeMeal)
admin.site.register(HomemadeMeal)
admin.site.register(Recipe)
admin.site.register(RecipeIngredient)
admin.site.register(KcalIn)
