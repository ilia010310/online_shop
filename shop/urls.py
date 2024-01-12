from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.items_list, name='item_list'),
    path('<slug:name>/', views.item_detail, name='item_detail'),


]