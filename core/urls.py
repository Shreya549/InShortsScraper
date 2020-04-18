from django.urls import path

from .views import Scraper


# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('', Scraper.as_view()),
]