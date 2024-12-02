from django.urls import path
from . import views

app_name = 'crops'

urlpatterns = [
    path('', views.crop_list, name='crop_list'),
    path('add/', views.crop_add, name='crop_add'),
    path('<int:crop_id>/', views.crop_detail, name='crop_detail'),
    path('<int:crop_id>/edit/', views.crop_edit, name='crop_edit'),
    path('<int:crop_id>/record/', views.growth_record_add, name='growth_record_add'),
    path('inventory/', views.inventory_list, name='inventory_list'),
    path('inventory/add/', views.inventory_add, name='inventory_add'),
    path('harvest/', views.harvest_list, name='harvest_list'),
    path('harvest/add/<int:crop_id>/', views.harvest_add, name='harvest_add'),
    path('inventory/<int:inventory_id>/edit/', views.inventory_edit, name='inventory_edit'),
] 