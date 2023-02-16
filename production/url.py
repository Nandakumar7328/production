from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.contrib import admin
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('admin/', admin.site.urls),
    path('updateData/<int:id>',views.updateData,name='updateData'),
    path('deleteData/<int:id>',views.deleteData,name='deleteData'),
    path('dashboard',views.dashboard, name='dashboard'),
    path('home',views.return_home, name='return_home')
]
