
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.main, name="home"),
    path('delete/<int:id>/', views.Delete, name="delete"),
    path('edit/<int:id>/', views.Edit, name="edit")
]
