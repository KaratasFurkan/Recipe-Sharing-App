from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .forms import RecipeForm
from .models import Recipe


class RecipeListView(ListView):
    model = Recipe
    context_object_name = "recipes"
    template_name = "home.html"


class ShareView(CreateView):
    model = Recipe
    form_class = RecipeForm
    success_url = reverse_lazy("home")
    template_name = "share.html"


def detail(request):
    return render(request, "detail.html")
