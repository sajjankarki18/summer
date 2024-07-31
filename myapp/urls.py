from django.urls import path
from .import views, auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('addPhoto/', views.addPhoto, name='addPhoto'),
    path('photo/<str:pk>', views.photo, name='photo'),
    path('deletePhoto/<str:pk>/', views.deletePhoto, name='deletePhoto'),
    
    
    # authentication views
    path('loginUser/', auth_views.loginUser, name='loginUser'),
    path('logoutUser/', auth_views.logoutUser, name='logoutUser'),
    path('registerUser/', auth_views.registerUser, name='registerUser')
]