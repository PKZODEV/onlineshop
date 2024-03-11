from django.urls import path
from theme import views

appname = 'theme'

urlpatterns = [
    path('homepage', views.homepage,name='homepage')
]