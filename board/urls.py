from django.urls import path
from .views import *
from . import views

app_name = 'board'

urlpatterns = [
    path('home/', board_list),
    path('home/detail/<int:pk>/',board_detail),
    path('home/region/<str:region>/', board_region),

]