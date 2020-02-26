from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import SignupForm


class Signup(CreateView):
    model = User
    form_class = SignupForm
    template_name = "signup.html"
    success_url = reverse_lazy("home")
