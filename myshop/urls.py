from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('categories/', views.categories),
    path('category/<str:category_name>/', views.category),
    path('item/<int:item_id>/', views.item)
]