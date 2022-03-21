from django.shortcuts import render

# Create your views here.


def recipe_list_view(request, id=None):
    return 

def recipe_detail_view(request, id=None):
    return 

def recipe_create_view(request, id=None):
    form = RecipeForm(request.POST or None)
    return

def recipe_update_view(request, id=None):
    form = RecipeForm(request.POST or None)
    return 