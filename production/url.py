from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    # path('addData',views.addData, name='addData'),
    path('updateData/<int:id>',views.updateData,name='updateData'),
    path('deleteData/<int:id>',views.deleteData,name='deleteData')
]
