from django.db.models import Count
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

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


class RecipeDetailView(DetailView):
    model = Recipe
    context_object_name = "recipe"
    pk_url_kwarg = "ingredient_pk"
    template_name = "detail.html"


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
