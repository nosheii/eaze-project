from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world, name='hello_world'),
    path('oppdaterNavn/', views.oppdaterNavn, name='oppdaterNavn'),
]
