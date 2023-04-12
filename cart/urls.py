from django.urls import path
from . import views


urlpatterns = [
    path('', views.cart, name= 'cart'),
    path('add_cart_item/<int:product_id>/', views.add_cart_item, name= 'add_cart_item'),
    path('remove_cart_item/<int:product_id>/<int:cart_item_id>/', views.remove_cart_item, name= 'remove_cart_item'),
    path('delete_cart_item/<int:product_id>/<int:cart_item_id>/', views.delete_cart_item, name= 'delete_cart_item'),
]