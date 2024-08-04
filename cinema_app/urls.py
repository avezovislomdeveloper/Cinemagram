from django.urls import path
from . import views

app_name = 'cinema_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('base/', views.base, name='base'),
    path('movies/', views.movie, name='movie'),
    path('like/', views.like, name='like'),
    path('fav/<int:pk>/', views.favourite_add, name='favourite_add'),
    path('favourites_list/', views.favourites_list, name='favourite_list'),
    path('movie_comment/', views.movie_comment, name='movie_comment'),
    
    
    
    
]