from django.urls import path
from .import views

urlpatterns = [
    path('',views.book_list,name='book_list'),
    path('book/create',views.book_create,name='book_create'),
    path('book/<id>/update',views.book_update,name='book_update'),
    path('book/<id>/delete',views.book_delete,name='book_delete'),
]
