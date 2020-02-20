from django.db.models import Count
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .forms import RecipeForm
from .models import Ingredient, Recipe


class RecipeListView(ListView):
    model = Recipe
    ordering = "-created_at"
    context_object_name = "recipes"
    extra_context = {
        "ingredients": Ingredient.objects.annotate(
            recipe_count=Count("recipe")
        ).order_by("-recipe_count")[:5]
    }
    template_name = "recipes.html"


class ShareView(CreateView):
    model = Recipe
    form_class = RecipeForm
    success_url = reverse_lazy("home")
    template_name = "share.html"


def detail(request):
    return render(request, "detail.html")


class ListByIngredientView(ListView):
    model = Recipe
    ordering = "-created_at"
    context_object_name = "recipes"
    extra_context = {
        "ingredients": Ingredient.objects.annotate(
            recipe_count=Count("recipe")
        ).order_by("-recipe_count")[:5]
    }
    template_name = "recipes.html"

    def get_queryset(self):
        return Ingredient.objects.get(pk=self.kwargs["ingredient_pk"]).recipe_set.all()
