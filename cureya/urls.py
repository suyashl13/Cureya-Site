from django.urls import path
from cureya.views import home, about, service, team, team_slug, contact, books, connect_us

urlpatterns = [
    path('', home),
    path('about/', about),
    path('service/', service),
    path('team/', team),
    path('team/<str:id>/', team_slug),
    path('contact/', contact),
    path('books/', books),
    path('connect/', connect_us)
]
