from django.urls import path
from .views import inscription,connexion,profile

urlpatterns = [
    path('', inscription),
    path('login/', connexion),
    path('profil/', profile,name='profil'),


   
]
