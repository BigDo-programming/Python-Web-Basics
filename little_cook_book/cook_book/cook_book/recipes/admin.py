from django.contrib import admin

from cook_book.recipes.models import Recipe, Ingredient, Measure


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'food_type', 'get_ingredients',)

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    pass


@admin.register(Measure)
class MeasureAdmin(admin.ModelAdmin):
    pass
