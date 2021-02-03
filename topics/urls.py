from django.urls import path

from topics import views

urlpatterns = [path("", views.test_cookies)]
