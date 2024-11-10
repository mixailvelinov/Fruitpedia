from django.urls import path
from django.urls.conf import include

from fruits import views

urlpatterns = [
    path('create/', views.CreateFruit.as_view(), name='fruit-create'),
    path('<int:id>/', include([
        path('details/', views.details_fruit, name='fruit-details'),
        path('edit/', views.EditFruit.as_view(), name='fruit-edit'),
        path('delete/', views.delete_fruit, name='fruit-delete'),
    ]))
]