from django.urls import path
from blog import views

urlpatterns = [
    path('', views.index),
    path('<int:pk>/', views.single_post_page),
    path('new/', views.post_new),
    path('restaurant/', views.restaurant),
    path('restaurant/<int:pk>/', views.restaurant_page),
    path('restaurant/new/', views.restaurant_new),

]