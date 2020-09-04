from django.urls import path
from . import views


urlpatterns = [
    path('', views.board_list, name= 'board_list'),
    path('rule/', views.rule, name='rule'),
    path('create_user/', views.Create_user, name='create_user'),
    path('after_create_user/', views.after_create_user, name='after_create_user'),
    path('create_thread/', views.create_thread, name='create_thread'),
    path('board/<int:pk>/', views.board, name='board'),
]