from django.urls import path
from music import views

urlpatterns = [
    path('', views.home, name ='home'),
    path('author/', views.author, name ='author'),
    path('search/', views.search_basic, name ='search_basic'),
    path('new/', views.create_music, name ='create_music'),
    path('update/<int:id>', views.update_music, name = 'update_music'),
    path('delete/<int:id>', views.delete_music, name = 'delete_music'),
    path('list/', views.list_music, name = 'list_musics'),
]