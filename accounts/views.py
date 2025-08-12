from django.shortcuts import render
from django.views.generic import FormView, UpdateView
from .forms import UserForm, CreateProfileForm
from django.utils import timezone
from accounts.models import User, Profile


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


from django.views.generic.edit import UpdateView

from django.utils import timezone
from django.views.generic.edit import UpdateView
from .models import Profile
from .forms import CreateProfileForm


class EditProfileView(UpdateView):
    model = Profile
    form_class = CreateProfileForm
    template_name = "registration/edit_profile.html"
    success_url = "/exams/"

    def get_object(self, queryset=None):
        return Profile.objects.get(username=self.request.user)

    def form_valid(self, form):
        profile = form.save(commit=False)
        profile.username = self.request.user
        profile.updated_date = timezone.now()
        profile.save()
        return super().form_valid(form)
