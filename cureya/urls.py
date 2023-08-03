from django.urls import path
from cureya.views import home, about

urlpatterns = [
    path('', home),
    path('about/', about)
]