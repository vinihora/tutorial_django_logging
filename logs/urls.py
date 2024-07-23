from . import views
from django.urls import path

urlpatterns = [
    path("log/", views.TestView.as_view())
]