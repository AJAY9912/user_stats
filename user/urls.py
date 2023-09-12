from django.urls import path
from .views import index, signup, dashboard

urlpatterns = [
    path('', index, name='home'),
    path('signup/', signup, name='signup'),
    path('dashboard/', dashboard, name='dashboard'),

    # Add more URL patterns as needed.
]
