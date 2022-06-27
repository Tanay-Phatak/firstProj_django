from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('add/addrecord/', views.addrecord, name='addrecord'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
    path('disp/', views.disp, name='disp'),
    path('search/', views.search, name='search'),
    path('delete/', views.delete, name='delete'),
    path('all-data/', views.AllData, name='all-data')
]