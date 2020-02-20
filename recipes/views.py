from django.db.models import Count
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .forms import RecipeForm
from .models import Ingredient, Recipe


class RecipeListView(ListView):
    model = Recipe
    queryset = Recipe.objects.order_by("-created_at")
    context_object_name = "recipes"
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ingredients"] = Ingredient.objects.annotate(
            recipe_count=Count("recipe")
        ).order_by("-recipe_count")[:5]
        return context


class ShareView(CreateView):
    model = Recipe
    form_class = RecipeForm
    success_url = reverse_lazy("home")
    template_name = "share.html"


def detail(request):
    return render(request, "detail.html")
