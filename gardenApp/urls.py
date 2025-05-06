from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'), 
    path('notebook/', views.notebook_list, name='notebook_list'),
    path('notebook/create/', views.notebook_create, name='notebook_create'),
    path('notebook/edit/<int:id>/', views.notebook_edit, name='notebook_edit'),
    path('notebook/delete/<int:id>/', views.notebook_delete, name='notebook_delete'),

]