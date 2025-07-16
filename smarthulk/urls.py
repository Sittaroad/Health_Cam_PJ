from django.urls import path
from smarthulk import views

urlpatterns = [
    path('',views.index,),
    path('detection',views.detection),
    path('static',views.static),
    path('settings', views.settings),
]