from django.urls import path
from smarthulk import views

urlpatterns = [
    path('',views.index,),
    path('detection',views.detection),
    path('analytics',views.analytics),
    path('settings', views.settings),
]