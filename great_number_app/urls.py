from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('guessed_num', views.guessed_num),
    path('leader_board', views.leader_board),
    path('log_winner', views.log_winner),
]