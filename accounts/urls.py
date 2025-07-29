from django.urls import path, include
from . import views


urlpatterns = [
    # urls login logout change password
    path("", include("django.contrib.auth.urls")),
    # url signup
    path("signup/", views.SignupView.as_view(), name="signup"),
]