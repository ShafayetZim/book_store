from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('add/', views.add_book, name='add_book'),
    path('add_to_cart/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
    path('process_order/', views.process_order, name='process_order'),
    path('api/books/', views.api_book_list, name='api_book_list'),
    path('api/add_book/', views.api_add_book, name='api_add_book'),
    path('api/orders/', views.api_order_list, name='api_order_list'),
    path('api/add_order/', views.api_add_order, name='api_add_order'),
]
