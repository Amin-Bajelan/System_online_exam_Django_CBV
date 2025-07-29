from django.shortcuts import render
from django.views.generic import FormView
from .forms import UserForm
from django.utils import timezone


# Create your views here.


class SignupView(FormView):
    # view for signup
    template_name = "registration/signup.html"
    form_class = UserForm
    success_url = "/accounts/login/"

    def form_valid(self, form):
        form.create_date = timezone.now()
        form.save()
        return super().form_valid(form)
