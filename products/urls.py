from django.urls import path

from . import views
app_name = 'products'
urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('get_cart/', views.get_cart, name='get_cart'),
    path('add_to_cart/<uuid:product_id>/', views.add_to_cart, name='add_to_cart'),
]