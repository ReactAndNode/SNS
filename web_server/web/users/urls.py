from django.conf.urls import url
from django.urls import path

from users import views

# we can have url keyword for matching
urlpatterns = [
    url(r'^account_activation_sent/$', views.account_activation_sent, name='account_activation_sent'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
]
