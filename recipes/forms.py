from django import forms

from .models import Recipe

class RecipeFrom(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'directions']