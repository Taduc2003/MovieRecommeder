from django.urls import path
from .views import api_suggestions

urlpatterns = [
    path('api/suggestions/', api_suggestions, name='api_suggestions'),
]
