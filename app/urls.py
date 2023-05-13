from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('', views.index, name='index'), #/user
    path('add/', views.add, name='add'), #/user/add
    path('update/<int:pk>/', views.update, name='update'), #/user/update
    path('delete/<int:pk>/', views.delete, name='delete'), #/user/delete
]