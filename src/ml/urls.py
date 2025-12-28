from django.urls import path
from .views import api_recommend_for_user

urlpatterns = [
    path('api/ml/suggestions/', api_recommend_for_user, name='api_recommend_for_user'),
]