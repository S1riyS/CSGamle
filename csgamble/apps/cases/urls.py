from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('case/<str:case_name>/', views.case)
]