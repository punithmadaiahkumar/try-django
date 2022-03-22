from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404

from .forms import RecipeForm
from .models import Recipe

# Create your views here.

@login_required
def recipe_list_view(request):
    qs = Recipe.objects.filter(user=request.user)
    context = {
        "object_list": qs
    }
    return render(request, "recipes/list.html", context)


@login_required
def recipe_detail_view(request, id=None):
    obj = get_object_or_404(Recipe, id=id, user=request.user)
    context = {
        "object": obj
    }
    return render(request, "recipes/detail.html", context)


@login_required
def recipe_create_view(request):
    form = RecipeForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return redirect(obj.get_absolute_url())
    return


@login_required
def recipe_update_view(request, id=None):
    form = RecipeForm(request.POST or None)
    obj = get_object_or_404(Recipe, id=id, user=request.user)
    context = {
        "form": form,
        "object": obj
    }
    return render(request, "recipes/detail.html", context)