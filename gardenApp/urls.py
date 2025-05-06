from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
urlpatterns = [
    # path('', views.index, name='index'), 
    path('', views.notebook_list, name='notebook_list'),
    path('notebook/create/', views.notebook_create, name='notebook_create'),
    path('notebook/edit/<int:id>/', views.notebook_edit, name='notebook_edit'),
    path('notebook/delete/<int:id>/', views.notebook_delete, name='notebook_delete'),

    path('login/', auth_views.LoginView.as_view(template_name='password_protect.html'), name='login'),
    path("password/", views.password_protect, name="password_protect"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)