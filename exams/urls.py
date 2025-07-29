from django.urls import path
from . import views

urlpatterns = [
    # main page
    path('', views.IndexView.as_view(), name='index'),
]