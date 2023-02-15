from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('updateData/<int:id>',views.updateData,name='updateData'),
    path('deleteData/<int:id>',views.deleteData,name='deleteData'),
    path('dashboard',views.dashboard, name='dashboard'),
    path('home',views.return_home,name='return_home')
]
