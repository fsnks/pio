from django.urls import path

from . import views

urlpatterns = [
     path('',views.homeon, name='homeon'),
     path('addin',views.addin, name='addin'),
     path('adddzz',views.adddzz, name='adddzz')
]