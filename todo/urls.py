from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('add', views.create_todo, name="create_todo"),
    path('delete/<int:id>', views.delete_todo, name='delete_todo'),
    path('search', views.search_todo, name='search_todo'),
]