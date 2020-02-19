from django import forms

from .models import Recipe


class RecipeForm(forms.ModelForm):
    description = forms.CharField(
        # TODO: handle in css
        widget=forms.Textarea(attrs={"style": "resize:none;"})
    )

    class Meta:
        model = Recipe
        fields = ["name", "image", "description", "difficulty", "ingredients"]
