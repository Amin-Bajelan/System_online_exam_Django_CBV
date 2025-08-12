from django.urls import path, include
from . import views


urlpatterns = [
    # urls login logout change password
    path("", include("django.contrib.auth.urls")),
    # url signup for create user and profile by signal
    path("signup/", views.SignupView.as_view(), name="signup"),
    # url edite profile info
    path('accounts/edit_profile/', views.EditProfileView.as_view(), name='edit_profile'),
]