from django.urls import path

from .views import register, login, home, add_card, ticket, logout

urlpatterns = [
    path('register', register),
    path('home', home),
    path('login', login),
    path('add-card', add_card, name='card'),
    path('buy-ticket', ticket),
    path('logout', logout)
]
