from common import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.Dashboard.as_view(), name='dashboard'),
]